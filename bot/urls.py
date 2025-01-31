from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'bot'

urlpatterns = [
        path('dashboard/', views.dashboard, name='dashboard'),

]
