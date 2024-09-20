from django.urls import path
from .views import update_expense_view

urlpatterns = [
    path('update/', update_expense_view, name='update_expense'),
]