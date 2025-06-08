"""Mentor model linked to Nest User."""

from __future__ import annotations

from django.db import models
from apps.nest.models.user import User


class Mentor(models.Model):
    """Mentor model storing mentor-specific details."""

    class Meta:
        db_table = "nest_mentors"
        verbose_name_plural = "Mentors"
        ordering = ["user__username"]

    user = models.OneToOneField(
        User,
        verbose_name="User",
        on_delete=models.CASCADE,
        related_name="mentor_profile",
    )

    tech_stack = models.JSONField(
        verbose_name="Tech Stack",
        default=list,
        blank=True,
        null=True,
        help_text="List of technologies the mentor is proficient in.",
    )

    domains_of_mentorship = models.JSONField(
        verbose_name="Domains of Mentorship",
        default=list,
        blank=True,
        null=True,
        help_text="Areas or domains the mentor provides guidance in.",
    )

    years_of_experience = models.PositiveIntegerField(
        verbose_name="Years of Experience"
    )
    mentee_limit = models.PositiveIntegerField(
        verbose_name="Mentee Limit",
        help_text="Maximum number of mentees a mentor can handle at once.",
    )
    active_mentees = models.PositiveIntegerField(
        verbose_name="Active Mentees",
        help_text="Current number of mentees under this mentor.",
    )
    availability = models.BooleanField(
        default=True,
        verbose_name="Availability",
        help_text="Whether the mentor is currently available for mentoring.",
    )

    mentees = models.ManyToManyField(
        "nest.Contributor",
        related_name="mentors",
        blank=True,
    )

    projects = models.ManyToManyField(
        "owasp.Project",
        verbose_name="Projects",
        blank=True,
    )

    def save(self, *args, **kwargs):
        """Ensure user role is set to mentor and no conflicting role exists."""
        if self.user.role and self.user.role != "mentor":
            raise ValueError("User already has a different role assigned!")
        self.user.role = "mentor"
        self.user.save()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        """Return username as string representation."""
        return self.user.username
