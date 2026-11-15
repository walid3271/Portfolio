from django.urls import path, include

urlpatterns = [
    path('', include('base.urls')),
]

handler404 = 'base.views.page_not_found'
