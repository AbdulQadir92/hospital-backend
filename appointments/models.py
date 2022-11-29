from django.db import models
from base.models import *


# Create your models here.
class Appointment(BaseModel):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    service = models.CharField(max_length=255, null=True, blank=True)
    doctor = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    time = models.CharField(max_length=255)

    def __str__(self):
        return self.name
