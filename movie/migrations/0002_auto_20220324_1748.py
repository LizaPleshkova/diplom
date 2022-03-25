# Generated by Django 3.2 on 2022-03-24 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviecomposition',
            old_name='id_movie',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='moviecomposition',
            old_name='id_person',
            new_name='person',
        ),
        migrations.AlterField(
            model_name='moviestudios',
            name='studio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ms_studio', to='movie.studio'),
        ),
    ]