import axios from "axios";

const resolveApiBase = () => {
  const envBase = import.meta.env.VITE_API_URL;
  if (typeof envBase === "string" && envBase.trim()) {
    return envBase.replace(/\/$/, "");
  }
  if (typeof window !== "undefined" && window.location?.origin) {
    return window.location.origin.replace(/\/$/, "");
  }
  return "http://127.0.0.1:8000";
};

const API_BASE = resolveApiBase();

/**
 * Plain axios client for login/refresh only — no auth interceptors.
 * Prevents infinite refresh loops when refresh returns 401.
 */
const authClient = axios.create({
  baseURL: `${API_BASE}/api/v1/`,
  timeout: 30000,
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
});

export default authClient;
