# Generated by Django 5.0.3 on 2024-03-13 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waiter',
            name='orders',
        ),
    ]