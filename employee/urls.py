from django.urls import path
from . import views

urlpatterns = [
    path('logs/', views.employee_log, name='employee_log'),
]