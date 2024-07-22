
from django.urls import path
from .views import ResearchAPIView

urlpatterns = [
    path('research/', ResearchAPIView.as_view(), name='learning-type'),
]
