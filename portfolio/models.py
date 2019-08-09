from django.db import models

# Create your models here.


class Portfolio(models.Model):
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    title = models.CharField(max_length=100)
    job = models.CharField(max_length=50)
    brief_info = models.CharField(max_length=250, blank=True)
    description = models.TextField()
    rating = models.IntegerField(blank=True)
    company = models.CharField(max_length=50, blank=True)
    site = models.URLField(blank=True)
    date = models.DateField(blank=True)
    city = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title
