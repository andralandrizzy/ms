from django.contrib import admin

from . models import ContactForm, ContactInfo
# Register your models here.

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'contact_date')
    list_display_links = ('id', 'name', 'email', 'contact_date')
    search_fields = ('name', 'email')
    list_per_page = 25

admin.site.register(ContactForm, ContactFormAdmin)


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('city', 'state', 'zipcode','phone_number','business_email')
    list_display_links = ('city', 'state', 'zipcode','phone_number','business_email')
    search_fields = ('city', 'state','zipcode','phone_number','business_email')
    list_per_page = 20

admin.site.register(ContactInfo, ContactInfoAdmin)