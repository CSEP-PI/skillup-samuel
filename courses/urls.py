from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static
from .views import CoursesView

router = DefaultRouter()
router.register(f'cursos', CoursesView, basename='cursos')

urlpatterns = [
    path('', include(router.urls)),
] 