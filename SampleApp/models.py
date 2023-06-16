from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = 'students'


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=50)
    students = models.ManyToManyField(Student, related_name='courses')

    class Meta:
        db_table = 'courses'

