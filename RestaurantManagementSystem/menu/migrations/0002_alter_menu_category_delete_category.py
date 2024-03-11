# Generated by Django 5.0.3 on 2024-03-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.CharField(choices=[('appetizers', 'Appetizers'), ('main_course', 'Main Course'), ('beverages', 'Beverages'), ('desert', 'Desert')], max_length=30),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]