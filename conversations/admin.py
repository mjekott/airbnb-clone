from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """Message Admin Model"""

    list_display = (
        "__str__",
        "created",
    )


@admin.register(models.Conservation)
class ConservationAdmin(admin.ModelAdmin):
    """Conservation Admin Model"""

    list_display = ("__str__", "count_messages", "count_participants")
    filter_horizontal = ("participants",)
