from django.contrib import admin

from . models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_create')
    list_display_links = ('id', 'name', 'date_create')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Testimonial, TestimonialAdmin)
