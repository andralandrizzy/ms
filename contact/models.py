from django.db import models
from datetime import datetime
from phone_field import PhoneField


# Create your models here.
class ContactForm(models.Model):
    message = models.TextField(blank=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length = 200)
    contact_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    address_link = models.URLField(blank=True)
    street_num = models.CharField(max_length=100, blank=True)
    street_name = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=5, blank=True, default="33054")
    phone_number = PhoneField(blank=True, max_length=31, help_text='Contact phone number')
    flexibility = models.CharField(max_length=100, blank=True)
    business_email = models.CharField(max_length=80, blank=True)
    email_avail = models.CharField(max_length=100, blank=True)

