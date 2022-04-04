# Generated by Django 3.2 on 2022-03-31 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_user_birth_date'),
        ('cinema', '0005_seat_number_row'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sector',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='BookingHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('Delete', 'DELETE'), ('Create', 'CREATE'), ('Update', 'UPDATE')], max_length=7, null=True, verbose_name='Type of action')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=1000, null=True)),
                ('datetime_book', models.DateTimeField()),
                ('action_time', models.DateTimeField(auto_now=True)),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_seat', to='cinema.seat')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_ms', to='cinema.moviesession')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.user')),
            ],
        ),
    ]