from django.contrib import admin
from . models import About_us, Timelines, Team, Client, Quote

# models register list

# AboutUs content Admin Class Registration
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id','name','email', )
    list_display_links = ('id', 'name', 'email',)
    search_fields = ('name', 'email')
    list_per_page = 25

admin.site.register(Quote, QuoteAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title')
    list_per_page = 25


admin.site.register(About_us, AboutAdmin)

# Timeline Admin Class Registration


class TimelinesAdmin(admin.ModelAdmin):
    list_display = ('id', 'years',)
    list_display_links = ('id', 'years',)
    list_filter = ('years',)
    search_fields = ('years',)
    list_per_page = 25


admin.site.register(Timelines, TimelinesAdmin)

# Team Member Admin Class Registration


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'carreer',)
    list_display_links = ('id', 'name', 'carreer',)
    list_filter = ('name', 'carreer',)
    search_fields = ('name', 'carreer',)
    list_per_page = 25


admin.site.register(Team, TeamAdmin)

# Clients List Model


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_link',)
    list_display_links = ('id', 'client_link',)
    list_filter = ('client_link',)
    search_fields = ('client_link',)
    list_per_page = 25


admin.site.register(Client, ClientAdmin)
