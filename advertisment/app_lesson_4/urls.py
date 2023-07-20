from django.urls import path
from .views import response_1

urlpatterns = [
    path('lesson_4', response_1)
]