from .views import email_sender
from django.urls import path

urlpatterns = [
    path('', email_sender, name="email_sender"),
]