from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static
from .views import CoursesViewSet, ClassCourseViewSet, EvaluationViewSet, ProgressViewSet, CursoSearchView

router = DefaultRouter()
router.register(f'cursos', CoursesViewSet, basename='cursos')
router.register(f'aulas', ClassCourseViewSet, basename='aulas') #get em aulas, filtrando ou não por cursos
router.register(f'avaliacao', EvaluationViewSet, basename='avaliacao')
router.register(f'progresso', ProgressViewSet, basename='progresso')

urlpatterns = [
    path('', include(router.urls)),
    path('buscar/', CursoSearchView.as_view()),
] 