from django.contrib import admin
from . models import Portfolio

# Register your models here.


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rating', 'company', 'site', 'date')
    list_display_links = ('id', 'title', 'rating', 'company', 'site', 'date')
    list_filter = ('title', 'rating', 'company', 'site', 'date')
    search_fields = ('title', 'rating', 'company', 'site', 'date')
    list_per_page = 25


admin.site.register(Portfolio, PortfolioAdmin)
