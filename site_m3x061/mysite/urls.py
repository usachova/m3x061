from django.urls import path
from .views import MainView, SubjectDetailView

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('<slug>', SubjectDetailView.as_view(), name='subject_detail'),
]
