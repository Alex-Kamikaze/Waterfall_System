# Generated by Django 5.1.1 on 2024-09-05 11:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_selling_system', '0005_alter_ticket_session_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessioninfo',
            name='datetime_of_session',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время сеанса'),
        ),
    ]
