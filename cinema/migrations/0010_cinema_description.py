# Generated by Django 3.2 on 2022-05-27 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0009_booking_id_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
