from django.urls import path
from .views import get_notes, delete_note   # 👈 ADD delete_note

urlpatterns = [
    path('', get_notes),
    path('delete/<int:id>/', delete_note),  # 👈 ADD THIS LINE
]