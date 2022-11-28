from django.db import models
from base.models import BaseModel


# Create your models here.
class Service(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='services_images')
    p1 = models.TextField(max_length=1000)
    p2 = models.TextField(max_length=1000, null=True, blank=True)
    p3 = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title
