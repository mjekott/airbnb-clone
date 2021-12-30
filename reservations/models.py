from django.db import models
from django.utils import timezone
from core import models as core_models

# Create your models here.


class Reservation(core_models.TimeStamedModel):

    """Reservation Model Definition"""

    STATUS_PENDING = "pending"
    STATUS_COMFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CANCELED, "Canceled"),
        (STATUS_COMFIRMED, "Confirmed"),
    )

    status = models.CharField(
        choices=STATUS_CHOICES, default=STATUS_PENDING, max_length=10
    )
    check_in = models.DateField()
    check_out = models.DateField()

    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )

    room = models.ForeignKey(
        "rooms.ROOM", related_name="reservations", on_delete=models.CASCADE
    )

    def in_progress(self):
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True

    def __str__(self):
        return f"{self.room}-{self.check_in}"
