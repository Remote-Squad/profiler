
from django.urls import path
from .views import ResearchAPIView, SocialResearchAPIView

urlpatterns = [
    path('research/', ResearchAPIView.as_view(), name='learning-type'),
    path('socials/', SocialResearchAPIView.as_view(), name='social-type'),
]
