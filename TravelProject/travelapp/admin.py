from django.contrib import admin
from .models import Tour, TourGuide, Ticket, Department, Arrival, Transport, Hotel, Customer, User
from django.urls import path
from django.utils.html import mark_safe
from django.template.response import TemplateResponse
from django.db.models import Count

class TourAdmin(admin.ModelAdmin):
    list_display = ("id", "name_tour", "active")

class TourGuideAdmin(admin.ModelAdmin):
    readonly_fields = ['imageTourGuide']

# class TravelappAdmin(admin.ModelAdmin):
#     search_fields = ['subject', 'category']
#     readonly_fields = ['image_view']
#
#     def image_view(self, course):
#         if course:
#             return mark_safe(
#                 '<img src="/static/{url}" width="120" />' \
#                     .format(url=course.image.name)
#             )
#
#     def get_urls(self):
#         return [
#                    path('course-stats/', self.stats_view)
#                ] + super().get_urls()
#
#     def stats_view(self, request):
#         c = Course.objects.filter(active=True).count()
#         stats = Course.objects.annotate(lesson_count=Count('my_lesson')).values('id', 'subject', 'lesson_count')
#
#         return TemplateResponse(request,
#                                 'admin/course-stats.html', {
#                                     'count': c,
#                                     'stats': stats
#                                 })

admin.site.register(User)
admin.site.register(Tour, TourAdmin)
admin.site.register(TourGuide)
admin.site.register(Ticket)
admin.site.register(Department)
admin.site.register(Arrival)
admin.site.register(Transport)
admin.site.register(Hotel)
admin.site.register(Customer)
