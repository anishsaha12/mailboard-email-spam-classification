from django.db import models
from employee.models import Employee

class Mail(models.Model):
    mail_of_emp = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE)
    mail_from_id = models.EmailField(max_length=75)
    mail_to = models.CharField(max_length=255)
    mail_cc = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    phishing = models.CharField(max_length=15,blank=True, null=True)
    body = models.TextField()
    received_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject + " - " + self.created_at.strftime("%Y-%m-%d %H:%M:%S")
