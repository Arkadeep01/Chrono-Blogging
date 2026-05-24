import axios from 'axios';
import { clearAuthSession, getRefreshToken, isAccessTokenExpired, setAuthUser } from './auth';
import { API_BASE_URL } from './constants';
import Cookies from 'js-cookie';
import { useAuthStore } from '../store/auth';

let refreshPromise = null;

// Define a custom Axios instance creator function
const useAxios = () => {

    // CREATE AXIOS INSTANCE
    const axiosInstance = axios.create({
        baseURL: API_BASE_URL,
    });

    // REQUEST INTERCEPTOR
    axiosInstance.interceptors.request.use(
        async (req) => {

            // Always get the latest tokens (avoid stale closure)
            let accessToken = Cookies.get('access_token');
            let refreshToken = Cookies.get('refresh_token') || useAuthStore.getState().refreshToken;

            // CHECK TOKEN EXPIRY
            if (accessToken && !isAccessTokenExpired(accessToken)) {
                req.headers.Authorization = `Bearer ${accessToken}`;
                return req;
            }

            if (refreshToken) {
                try {
                    if (!refreshPromise) {
                        refreshPromise = getRefreshToken(refreshToken).finally(() => {
                            refreshPromise = null;
                        });
                    }
                    const response = await refreshPromise;
                    setAuthUser(response.access, response.refresh || refreshToken);
                    req.headers.Authorization = `Bearer ${response.access}`;
                    return req;
                } catch (error) {
                    console.error('Token refresh failed:', error);
                    clearAuthSession();
                    return req;
                }
            }
            return req;
        },
        (error) => Promise.reject(error)
    );

    // RESPONSE INTERCEPTOR (GLOBAL ERROR HANDLING)
    axiosInstance.interceptors.response.use(
        (response) => response,
        async (error) => {

            // If unauthorized → force logout
            if (error.response?.status === 401 && !error.config?.url?.includes('user/token/refresh')) {
                clearAuthSession();
            }

            return Promise.reject(error);
        }
    );

    return axiosInstance;
};

export default useAxios;
