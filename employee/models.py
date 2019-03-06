from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    email_id = models.EmailField()
    latest_uid = models.IntegerField()

    photograph = models.ImageField(blank=True, null=True, upload_to='avatar/')

    is_active = models.BooleanField(default=True)

    
    #meta

    def __str__(self):
        return self.first_name + " " + self.last_name