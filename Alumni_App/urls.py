from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('jobs/', views.jobs, name='jobs'),
    path('events/', views.events, name='events'),
    path('networking/', views.networking, name='networking'),
]
