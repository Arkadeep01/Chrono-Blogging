from django.conf import settings


def build_media_url(request, file_field):
    """
    Return an absolute URL for a FileField/ImageField so the frontend
    (on a different origin) can load uploaded media correctly.
    """
    if not file_field:
        return None

    try:
        url = file_field.url
    except (ValueError, AttributeError):
        return None

    if not url:
        return None

    if url.startswith(("http://", "https://")):
        return url

    if not url.startswith("/"):
        url = f"/{url}"

    if request:
        return request.build_absolute_uri(url)

    return f"{settings.SITE_URL}{url}"
