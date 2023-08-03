from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    favorite_sport = models.CharField(max_length=100, default='unknown')

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
