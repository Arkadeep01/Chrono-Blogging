import axios from "axios";
import Cookies from "js-cookie";
import {
  clearAuthSession,
  getRefreshToken,
  isAccessTokenExpired,
} from "./auth";

const ACCESS_TOKEN_COOKIE = "access_token";
const REFRESH_TOKEN_COOKIE = "refresh_token";

const apiInstance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}/api/v1/`,
  timeout: 50000,
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
});

let refreshPromise = null;

const isRefreshRequest = (config) =>
  config?.url?.includes("user/token/refresh");

const refreshAccessToken = async (refreshToken) => {
  if (!refreshPromise) {
    refreshPromise = getRefreshToken(refreshToken).finally(() => {
      refreshPromise = null;
    });
  }
  return refreshPromise;
};

apiInstance.interceptors.request.use(
  (config) => {
    const accessToken = Cookies.get(ACCESS_TOKEN_COOKIE);

    // Do not send expired/invalid tokens on public routes (avoids 401 storms)
    if (accessToken && !isAccessTokenExpired(accessToken)) {
      config.headers.Authorization = `Bearer ${accessToken}`;
    }

    return config;
  },
  (error) => Promise.reject(error)
);

apiInstance.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (!originalRequest || isRefreshRequest(originalRequest)) {
      return Promise.reject(error);
    }

    if (error.response?.status !== 401 || originalRequest._retry) {
      return Promise.reject(error);
    }

    originalRequest._retry = true;

    const refreshToken = Cookies.get(REFRESH_TOKEN_COOKIE);

    if (!refreshToken) {
      clearAuthSession();
      delete originalRequest.headers.Authorization;
      return apiInstance(originalRequest);
    }

    try {
      const response = await refreshAccessToken(refreshToken);

      Cookies.set(ACCESS_TOKEN_COOKIE, response.access, {
        expires: 1,
        sameSite: "Lax",
        secure: import.meta.env.PROD,
        path: "/",
      });
      Cookies.set(REFRESH_TOKEN_COOKIE, response.refresh || refreshToken, {
        expires: 50,
        sameSite: "Lax",
        secure: import.meta.env.PROD,
        path: "/",
      });

      originalRequest.headers.Authorization = `Bearer ${response.access}`;
      return apiInstance(originalRequest);
    } catch (refreshError) {
      clearAuthSession();
      delete originalRequest.headers.Authorization;

      // Retry once without auth so public endpoints still load
      if (!originalRequest._noAuthRetry) {
        originalRequest._noAuthRetry = true;
        return apiInstance(originalRequest);
      }

      return Promise.reject(refreshError);
    }
  }
);

export default apiInstance;
