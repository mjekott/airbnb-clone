from django.db import models
from core import models as core_models

# Create your models here.


class Conservation(core_models.TimeStamedModel):
    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return self.created


class Message(core_models.TimeStamedModel):
    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conservation = models.ForeignKey("Conservation", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}-says: {self.message}"
