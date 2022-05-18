from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Subject

class MainView(View):
    def get(self, request, *args, **kwargs):
        subject = Subject.objects.all()
        return render(
            request,
            'mysite/home.html',
            context={
                'subject': subject
            }

        )

class SubjectDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        subject = get_object_or_404(Subject, url=slug)
        return render(request, 'mysite/subject_detail.html', context={
            'subject': subject
    })
