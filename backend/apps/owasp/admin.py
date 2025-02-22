"""OWASP app admin."""

from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from apps.owasp.models.chapter import Chapter
from apps.owasp.models.committee import Committee
from apps.owasp.models.event import Event
from apps.owasp.models.project import Project
from apps.owasp.models.snapshot import Snapshot


class GenericEntityAdminMixin:
    def custom_field_github_urls(self, obj):
        """Entity GitHub URLs."""
        urls = [
            f"<a href='https://github.com/{repository.owner.login}/"
            f"{repository.key}' target='_blank'>↗️</a>"
            for repository in (
                obj.repositories.all() if hasattr(obj, "repositories") else [obj.owasp_repository]
            )
        ]

        return mark_safe(" ".join(urls))  # noqa: S308

    def custom_field_owasp_url(self, obj):
        """Entity OWASP URL."""
        return mark_safe(  # noqa: S308
            f"<a href='https://owasp.org/{obj.key}' target='_blank'>↗️</a>"
        )

    def approve_suggested_leaders(self, request, queryset):
        """Approve all suggested leaders for selected entities."""
        for entity in queryset:
            suggestions = entity.suggested_leaders.all()
            entity.leaders.add(*suggestions)
            self.message_user(
                request,
                f"Approved {suggestions.count()} leader suggestions for {entity.name}",
                messages.SUCCESS,
            )

    custom_field_github_urls.short_description = "GitHub 🔗"
    custom_field_owasp_url.short_description = "OWASP 🔗"
    approve_suggested_leaders.short_description = "Approve all suggested leaders"


class LeaderEntityAdmin(admin.ModelAdmin, GenericEntityAdminMixin):
    """Admin class for entities that have leaders."""

    actions = ["approve_suggested_leaders"]
    filter_horizontal = ("suggested_leaders",)


class ChapterAdmin(LeaderEntityAdmin):
    autocomplete_fields = ("owasp_repository", "leaders")
    list_display = (
        "name",
        "region",
        "custom_field_owasp_url",
        "custom_field_github_urls",
    )
    list_filter = (
        "is_active",
        "country",
        "region",
    )
    search_fields = ("name", "key")


class CommitteeAdmin(LeaderEntityAdmin):
    autocomplete_fields = ("owasp_repository", "leaders")
    search_fields = ("name",)


class EventAdmin(admin.ModelAdmin, GenericEntityAdminMixin):
    autocomplete_fields = ("owasp_repository",)
    list_display = ("name",)
    search_fields = ("name",)


class ProjectAdmin(LeaderEntityAdmin):
    autocomplete_fields = (
        "organizations",
        "owasp_repository",
        "owners",
        "repositories",
        "leaders",
    )
    list_display = (
        "custom_field_name",
        "created_at",
        "updated_at",
        "stars_count",
        "forks_count",
        "commits_count",
        "releases_count",
        "custom_field_owasp_url",
        "custom_field_github_urls",
    )
    list_filter = (
        "is_active",
        "has_active_repositories",
        "level",
        "type",
    )
    ordering = ("-created_at",)
    search_fields = (
        "custom_tags",
        "description",
        "key",
        "languages",
        "leaders_raw",
        "name",
        "topics",
    )

    def custom_field_name(self, obj):
        """Project custom name."""
        return f"{obj.name or obj.key}"

    custom_field_name.short_description = "Name"


class SnapshotAdmin(admin.ModelAdmin):
    autocomplete_fields = (
        "new_chapters",
        "new_issues",
        "new_projects",
        "new_releases",
        "new_users",
    )
    list_display = (
        "start_at",
        "end_at",
        "status",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "status",
        "start_at",
        "end_at",
    )
    ordering = ("-start_at",)
    search_fields = (
        "status",
        "error_message",
    )


admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Committee, CommitteeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Snapshot, SnapshotAdmin)
