# Generated by Django 3.0.6 on 2020-05-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_auto_20200530_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='recivedorders',
            name='status',
            field=models.CharField(default='Ordered', max_length=65),
        ),
    ]
