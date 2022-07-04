from django.db import models

# from django.contrib.auth.models import User
# from django.utils import timezone

class Teacher(models.Model):
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200, null=True, blank=True)
    isu = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        patronymic = self.patronymic if self.patronymic else ''
        return self.surname + ' ' + self.name + ' ' + patronymic

class Subject(models.Model):
    slug = models.CharField(max_length=25)
    title = models.CharField(max_length=200)
    сontrol_type = models.CharField(max_length=200)
    # lector = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True, related_name='lector')
    # practice = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True, related_name='practice')
    # deadlines = models.TextField()

    def __str__(self):
        return self.title

class Student(models.Model):
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        patronymic = self.patronymic if self.patronymic else ''
        return self.surname + ' ' + self.name + ' ' + patronymic


