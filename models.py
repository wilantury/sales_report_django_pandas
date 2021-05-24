from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_student = models.BooleanField( default=False)
    is_teacher = models.BooleanField( default=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

class Materia(models.Model):
    name = models.CharField(max_length=60)
    id_materia = models.CharField(max_length=20)
    student = models.ManyToManyField(Student, related_name=Salon_materia)

class Score(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Salon(models.Model):
    id_salon = models.IntegerField(max_length=10)
    description = models.TextField()

class Salon_materia(models.Model):
    materia = models.ForeignKey(Materia)
    salon = models.ForeignKey(Salon)









 




