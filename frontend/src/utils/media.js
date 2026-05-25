/**
 * Resolve API media paths to full URLs on the backend host.
 * Falls back when the API returns relative paths like /media/image/...
 */
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

export function getMediaUrl(url, fallback = "") {
  if (!url) return fallback;
  if (typeof url !== "string") return fallback;

  const apiBase = resolveApiBase();

  if (
    url.startsWith("http://") ||
    url.startsWith("https://") ||
    url.startsWith("data:") ||
    url.startsWith("blob:")
  ) {
    try {
      const parsed = new URL(url);
      if (parsed.pathname.startsWith("/media/")) {
        return `${apiBase}${parsed.pathname}`;
      }
    } catch {
      return fallback;
    }
    return url;
  }

  const path = url.startsWith("/") ? url : `/${url}`;
  return `${apiBase}${path}`;
}
