from rest_framework import urls
from django.urls import path, include

urlpatterns = [
    path('', include('testapp.urls')),
    path('api-auth/', include(urls)),
]
