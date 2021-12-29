from django.db import models

# Create your models here.


class TimeStamedModel(models.Model):
    """Abstarct Time Stamp Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
