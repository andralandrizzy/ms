from django.db import models
from datetime import datetime

# Create your models here.


class Testimonial(models.Model):
    quote = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=100, blank=True)
    date_create = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
