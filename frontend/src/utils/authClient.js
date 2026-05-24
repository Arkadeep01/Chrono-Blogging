import axios from "axios";

/**
 * Plain axios client for login/refresh only — no auth interceptors.
 * Prevents infinite refresh loops when refresh returns 401.
 */
const authClient = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}/api/v1/`,
  timeout: 30000,
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
});

export default authClient;
