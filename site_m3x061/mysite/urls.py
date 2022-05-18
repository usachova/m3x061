from django.urls import path
from .views import MainView, SubjectDetailView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('blog/<slug>/', SubjectDetailView.as_view(), name='subject_detail'),
]
