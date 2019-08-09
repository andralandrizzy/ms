from django.db import models

# Create your models here.

# AboutUs Content Model

class Quote(models.Model):
    name  = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    message = models.TextField(blank = True)

    def  __str__(self):
        return self.name


class About_us(models.Model):
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

# Timeline Model


class Timelines(models.Model):
    years = models.CharField(max_length=100)
    time_info = models.TextField()

    def __str__(self):
        return self.years

# Our Team Member Model


class Team(models.Model):
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    name = models.CharField(max_length=100)
    carreer = models.CharField(max_length=100)
    description = models.TextField()
    facebook = models.URLField(max_length=100, blank=True)
    twitter = models.URLField(max_length=100, blank=True)
    instagram = models.URLField(max_length=100, blank=True)
    gmail = models.URLField(max_length=100, blank=True)

    def __str__(self):
        return self.name


# Our Clients List Model
class Client(models.Model):
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    client_link = models.URLField(max_length=100)
