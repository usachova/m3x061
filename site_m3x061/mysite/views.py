from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from .models import Subject, Student

class MainView(View):
    def get(self, request, *args, **kwargs):
        subjects = Subject.objects.all()
        students = Student.objects.all()
        return render(request, 'mysite/home.html', context={'subjects': subjects, 'students': students})

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'mysite/subject.html'
    context_object_name = 'subject'

