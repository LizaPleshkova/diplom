# Generated by Django 3.2 on 2022-04-13 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0006_auto_20220331_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='isBooked',
            field=models.BooleanField(default=False),
        ),
    ]
