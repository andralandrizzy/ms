from django.db import models
from fontawesome.fields import IconField
# Create your models here.


class Service(models.Model):
    icon = IconField()
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    job = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.job

    def summary(self):
        return self.description[:150]
