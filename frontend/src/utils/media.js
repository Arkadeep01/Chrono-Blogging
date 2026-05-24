/**
 * Resolve API media paths to full URLs on the backend host.
 * Falls back when the API returns relative paths like /media/image/...
 */
export function getMediaUrl(url, fallback = "") {
  if (!url) return fallback;
  if (typeof url !== "string") return fallback;

  if (
    url.startsWith("http://") ||
    url.startsWith("https://") ||
    url.startsWith("data:") ||
    url.startsWith("blob:")
  ) {
    return url;
  }

  const apiBase = (import.meta.env.VITE_API_URL || "http://127.0.0.1:8000").replace(
    /\/$/,
    ""
  );
  const path = url.startsWith("/") ? url : `/${url}`;
  return `${apiBase}${path}`;
}
