from rest_framework import serializers

from api.utils.media import build_media_url


class AbsoluteImageField(serializers.ImageField):
    """Serialize ImageField values as absolute URLs."""

    def to_representation(self, value):
        if not value:
            return None
        return build_media_url(self.context.get("request"), value)
