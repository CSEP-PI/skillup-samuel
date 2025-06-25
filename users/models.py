from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    STATUS_CHOICES = [
        ('A', 'Aluno'),
        ('I', 'Instrutor'),
        ('ADM', 'Administrador'),
    ]

    profile_img = models.ImageField(upload_to='imgs/', blank=True, null=True)
    cpf = models.CharField(max_length=11)
    status = models.CharField(max_length=3, default='A', choices=STATUS_CHOICES)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username