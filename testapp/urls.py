from django.urls import path

from . import views

urlpatterns = [
    path('', views.index.as_view()),
    path('refresh/', views.refresh.as_view()),
    path('send/', views.send.as_view())
]
