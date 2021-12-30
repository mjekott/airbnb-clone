from django.contrib import admin
from . import models
from django.utils.html import mark_safe

# Register your models here.


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    inlines = [
        PhotoInline,
    ]

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price", "host")},
        ),
        ("Times", {"fields": ("check_in", "check_out")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
    )

    ordering = ("name", "price", "bedrooms")

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "total_rating",
        "count_amenities",
        "count_photos",
    )

    list_filter = (
        "instant_book",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "host__superhost",
        "city",
        "country",
    )

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )
    raw_id_fields = ("host",)

    search_fields = ("^city", "^host__username")

    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = "No of Amenities"

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.RoomType, models.Amenity, models.HouseRule, models.Facility)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f"<img width='50' src='{obj.file.url}' alt='thumbnail' />")

    get_thumbnail.short_description = "Thumbnail"
