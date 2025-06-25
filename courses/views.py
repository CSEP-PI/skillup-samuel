from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Course, ClassCourse, Progress,Evaluation
from .serializers import CourseSerializer, ClassCourseSerializer, ProgressSerializer, EvaluationSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.status import *
from django.core import serializers

# Create your views here.
class CoursesViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CursoSearchView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        queryset = Course.objects.all()
        print(queryset.data)
        if queryset.exists():
            return Response(queryset)
        
        return Response({
            "message": "Nenhum resultado encontrado para sua busca"
        }, status=HTTP_404_NOT_FOUND)

class ClassCourseViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ClassCourse.objects.all()
    serializer_class = ClassCourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course']
    
class ProgressViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'course']

class EvaluationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer



