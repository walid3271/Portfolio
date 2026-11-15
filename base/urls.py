from django.urls import path
from django.views.generic import TemplateView

from .views import home, send_contact_email

urlpatterns = [
    path('', home, name='home'),
    path('contact/send/', send_contact_email, name='send_contact_email'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='application/xml')),
]
