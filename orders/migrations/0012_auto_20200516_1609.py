# Generated by Django 3.0.6 on 2020-05-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20200516_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='base',
        ),
        migrations.AddField(
            model_name='pizza',
            name='base',
            field=models.ManyToManyField(related_name='pizzatopping', to='orders.PizzaBase'),
        ),
    ]
