from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(prefix='users', viewset=views.UserViewSet, basename='user')
router.register(prefix='departments', viewset=views.DepartmentViewSet, basename='department')
router.register(prefix='tours', viewset=views.TourViewSet, basename='tour')

urlpatterns = [
    path('', include(router.urls)),
    path('oauth2-info/', views.AuthInfo.as_view()),
]