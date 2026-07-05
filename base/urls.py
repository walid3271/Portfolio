from django.urls import path
from .views import home, send_contact_email

urlpatterns = [
    path('', home),
    path('contact/send/', send_contact_email, name='send_contact_email'),
]
