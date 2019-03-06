# Generated by Django 2.1 on 2018-10-12 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee_latest_uid'),
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='mail_from_emp',
        ),
        migrations.AddField(
            model_name='mail',
            name='mail_of_emp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Employee'),
        ),
    ]