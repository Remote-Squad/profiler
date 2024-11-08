from django.urls import path
from .views import update_expense_view
from .views import extract_text

urlpatterns = [
    path('update/', update_expense_view, name='update_expense'),
    path('extract_text/', extract_text, name='extract_text'),
]


