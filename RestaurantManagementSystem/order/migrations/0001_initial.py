# Generated by Django 5.0.3 on 2024-03-11 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0002_alter_menu_category_delete_category'),
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('preparing', 'Preparing'), ('served', 'Served')], max_length=250)),
                ('timestamp', models.DateTimeField()),
                ('items', models.ManyToManyField(to='menu.menu')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.table')),
            ],
        ),
    ]
