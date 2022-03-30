from django.contrib import admin
from .models import Tour, TourGuide, Ticket, Department, Arrival, Transport, Hotel, Customer, User
from django.urls import path

class TourAdmin(admin.ModelAdmin):
    list_display = ("id", "name_tour", "active")

class TourGuideAdmin(admin.ModelAdmin):
    readonly_fields = ['imageTourGuide']



admin.site.register(User)
admin.site.register(Tour, TourAdmin)
admin.site.register(TourGuide)
admin.site.register(Ticket)
admin.site.register(Department)
admin.site.register(Arrival)
admin.site.register(Transport)
admin.site.register(Hotel)
admin.site.register(Customer)
