from rest_framework import serializers
from .models import Course, ClassCourse, Progress, Evaluation


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ClassCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassCourse
        fields = '__all__'

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = '__all__'

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'