from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Course
from .serializers import CourseSerializer
from rest_framework.response import Response

# Create your views here.
class CoursesView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer