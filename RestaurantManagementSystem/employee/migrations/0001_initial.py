# Generated by Django 5.0.3 on 2024-03-13 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=250)),
                ('shift', models.CharField(choices=[('morning', 'Morning'), ('day', 'Day'), ('evening', 'Evening')], max_length=250)),
                ('status', models.CharField(choices=[('free', 'Free'), ('usy', 'Busy')], default='free', max_length=10)),
            ],
        ),
    ]
