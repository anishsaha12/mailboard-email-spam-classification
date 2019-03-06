from django.urls import path
from . import views

urlpatterns = [
    path('', views.mail_inbox, name='mail_list'),
    path('inbox/', views.mail_inbox, name='mail_list'),
    path('compose/', views.mail_compose, name='mail_list'),
    path('stats/', views.mail_stats, name='mail_list'),
]