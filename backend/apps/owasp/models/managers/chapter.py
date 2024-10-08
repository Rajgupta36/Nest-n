"""OWASP app chapter managers."""

from django.db import models
from django.db.models import Q


class ActiveChaptertManager(models.Manager):
    """Active chapters."""

    def get_queryset(self):
        """Get queryset."""
        return (
            super()
            .get_queryset()
            .filter(is_active=True)
            .select_related("owasp_repository")
            .filter(
                owasp_repository__is_archived=False,
                owasp_repository__is_empty=False,
            )
        )

    @property
    def without_geo_data(self):
        """Return chapters that don't have geo data."""
        return self.get_queryset().filter(
            Q(latitude__isnull=True) | Q(longitude__isnull=True),
        )