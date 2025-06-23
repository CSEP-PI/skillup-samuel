from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    image = models.FileField(upload_to='media')
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=False, blank=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)

    class Meta:
        db_table = 'course'

    def __str__(self):
        return self.name

class ClassCourse(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='media/class/', null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'class_course'

    def __str__(self):
        return self.name

class Progress(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.FloatField(default=0)

    class Meta:
        db_table = 'progress'

    def __str__(self):
        return f'{self.user.username} - {self.course.name} - {self.progress}%'

class Evaluation(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'evaluation'

    def __str__(self):
        return f'{self.user.username} - {self.course.name} - {self.rating}'