from django.db import models
from core import models as core_models

# Create your models here.


class Conservation(core_models.TimeStamedModel):
    participants = models.ManyToManyField(
        "users.User", related_name="conservation", blank=True
    )

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "No of messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "No of participants"

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)

        return ", ".join(usernames)


class Message(core_models.TimeStamedModel):
    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conservation = models.ForeignKey(
        "Conservation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user}-says: {self.message}"
