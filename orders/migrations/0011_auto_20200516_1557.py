# Generated by Django 3.0.6 on 2020-05-16 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20200516_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='base',
        ),
        migrations.AddField(
            model_name='pizza',
            name='base',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='pizzabase', to='orders.PizzaBase'),
            preserve_default=False,
        ),
    ]