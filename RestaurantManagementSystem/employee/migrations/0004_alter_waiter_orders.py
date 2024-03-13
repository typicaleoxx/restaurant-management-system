# Generated by Django 5.0.2 on 2024-03-12 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_waiter_orders'),
        ('order', '0002_alter_order_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waiter',
            name='orders',
            field=models.ManyToManyField(null=True, related_name='waiters', to='order.order'),
        ),
    ]
