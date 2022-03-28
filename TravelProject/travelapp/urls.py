from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("users", views.UserViewSet, 'user')

urlpatterns = [
    path('', include(router.urls)),
    path('oauth2-info/', views.AuthInfo.as_view()),
]