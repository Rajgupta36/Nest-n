"""Nest app admin."""

from django.contrib import admin

from apps.nest.models.user import User
from apps.nest.models.contributor import Contributor
from apps.nest.models.mentor import Mentor


class UserAdmin(admin.ModelAdmin):
    ordering = ("username",)
    search_fields = ("email", "username")


admin.site.register(User, UserAdmin)
admin.site.register(Contributor)
admin.site.register(Mentor)
