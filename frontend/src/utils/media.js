/**
 * Resolve API media paths to full URLs on the backend host.
 * Falls back when the API returns relative paths like /media/image/...
 */
export function getMediaUrl(url, fallback = "") {
  if (!url) return fallback;
  if (typeof url !== "string") return fallback;

  const apiBase = (import.meta.env.VITE_API_URL || "http://127.0.0.1:8000").replace(
    /\/$/,
    ""
  );

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
