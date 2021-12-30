from django.db import models
from core import models as core_models
from rooms import models as room_models

# Create your models here.


class List(core_models.TimeStamedModel):
    """List Model Definition"""

    name = models.CharField(max_length=80)
    user = models.ForeignKey(
        "users.User", related_name="listings", on_delete=models.CASCADE
    )
    rooms = models.ManyToManyField(
        room_models.Room, related_name="listings", blank=True
    )

    def count_rooms(self):
        return self.rooms.count()

    count_rooms.short_description = "No of rooms"

    def __str__(self):
        return self.name
