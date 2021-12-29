from django.db import models
from core import models as core_models
from rooms import models as room_models

# Create your models here.


class List(core_models.TimeStamedModel):
    """List Model Definition"""

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rooms = models.ManyToManyField(room_models.Room, blank=True)

    def __str__(self):
        return self.name
