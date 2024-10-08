"""OWASP app project mixins."""

from apps.owasp.models.mixins.common import GenericEntityMixin


class ChapterIndexMixin(GenericEntityMixin):
    """Chapter index mixin."""

    @property
    def idx_country(self):
        """Return country for indexing."""
        return self.country

    @property
    def idx_created_at(self):
        """Return created at for indexing."""
        return self.owasp_repository.created_at

    @property
    def idx_geo_location(self):
        """Return geographic location for indexing."""
        return self.latitude, self.longitude

    @property
    def idx_meetup_group(self):
        """Return meetup group for indexing."""
        return self.meetup_group

    @property
    def idx_postal_code(self):
        """Return postal code for indexing."""
        return self.postal_code

    @property
    def idx_region(self):
        """Return region for indexing."""
        return self.region

    @property
    def idx_related_urls(self):
        """Return related URLs for indexing."""
        return self.related_urls

    @property
    def idx_suggested_location(self):
        """Return suggested location for indexing."""
        return self.suggested_location

    @property
    def idx_updated_at(self):
        """Return updated at for indexing."""
        return self.owasp_repository.updated_at

    @property
    def idx_url(self):
        """Return URL for indexing."""
        return self.owasp_url