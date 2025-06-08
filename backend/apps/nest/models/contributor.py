"""Contributor model linked to Nest User."""

from __future__ import annotations

from django.db import models
from apps.nest.models.user import User


class Contributor(models.Model):
    """Contributor model storing contributor-specific details."""

    class Meta:
        db_table = "nest_contributors"
        verbose_name_plural = "Contributors"
        ordering = ["user__username"]

    user = models.OneToOneField(
        User,
        verbose_name="User",
        on_delete=models.CASCADE,
        related_name="contributor_profile",
    )

    top_languages = models.JSONField(
        verbose_name="Top Languages",
        default=list,
        blank=True,
        null=True,
        help_text="Most frequently used programming languages.",
    )

    preferred_tech_stack = models.JSONField(
        verbose_name="Preferred Tech Stack",
        default=list,
        blank=True,
        null=True,
        help_text="Technologies the contributor prefers working with.",
    )

    interested_domains = models.JSONField(
        verbose_name="Interested Domains",
        default=list,
        blank=True,
        null=True,
        help_text="Domains or areas the contributor is interested in.",
    )

    issues_worked_on = models.PositiveIntegerField(verbose_name="Issues Worked On")
    prs_open = models.PositiveIntegerField(verbose_name="Open PRs")
    prs_merged = models.PositiveIntegerField(verbose_name="Merged PRs")

    projects = models.ManyToManyField(
        "owasp.Project",
        verbose_name="Projects",
        blank=True,
    )

    def save(self, *args, **kwargs):
        """Ensure user role is set to contributor and no conflicting role exists."""
        if self.user.role and self.user.role != "contributor":
            raise ValueError("User already has a different role assigned!")
        self.user.role = "contributor"
        self.user.save()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        """Return username as string representation."""
        return self.user.username
