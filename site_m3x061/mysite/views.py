from django.shortcuts import render
from django.views import View
from .models import Subject

class MainView(View):
    def get(self, request, *args, **kwargs):
        subjects = Subject.objects.all()
        return render(
            request,
            'mysite/home.html',
            context={
                'subjects': subjects
            }

        )
