from django.db import models
from django.db.models.deletion import SET_DEFAULT, SET_NULL
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


# Create your models here.
class AbstractItem(core_models.TimeStamedModel):
    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """Room Type Model Definition"""

    class Meta:
        verbose_name_plural = "Room Type"
        ordering = ["name"]


class Amenity(AbstractItem):
    """Amenity Type Model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """Facility Type Model Definition"""

    class Meta:
        verbose_name_plural = "Faclilities"


class HouseRule(AbstractItem):
    """House Rule Model Definition"""

    class Meta:
        verbose_name_plural = "House Rule"


class Room(core_models.TimeStamedModel):

    """Room Model Definition"""

    name = models.CharField(max_length=400)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    guests = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_type = models.ForeignKey(
        RoomType, blank=True, on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)

    def __str__(self):
        return self.name


class Photo(core_models.TimeStamedModel):
    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
