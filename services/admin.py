from django.contrib import admin
from . models import Service

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'job',)
    list_display_links = ('id', 'job',)
    list_filter = ('job',)
    search_fields = ('job',)
    list_per_page = 25


admin.site.register(Service, ServiceAdmin)
