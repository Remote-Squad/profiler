
from django.urls import path
from .views import LearningTypeAPIView

urlpatterns = [
    path('learning-type/', LearningTypeAPIView.as_view(), name='learning-type'),
]
