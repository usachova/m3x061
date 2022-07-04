from django.db import models

# from django.contrib.auth.models import User
# from django.utils import timezone


class Subject(models.Model):
    slug = models.CharField(max_length=25)
    title = models.CharField(max_length=200)
    сontrol_type = models.CharField(max_length=200)
    # lector = models.CharField(max_length=200)
    # lector_isu = models.CharField(max_length=200, null=True, blank=True)
    # content_lectures = models.TextField()
    # practice = models.CharField(max_length=200)
    # practice_isu = models.CharField(max_length=200, null=True, blank=True)
    # content_practice = models.TextField()
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
