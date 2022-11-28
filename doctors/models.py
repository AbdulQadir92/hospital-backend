from django.db import models
from base.models import BaseModel


# Create your models here.
class Doctor(BaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='doctors_images')
    designation = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
