# Generated by Django 5.1.1 on 2024-09-05 10:55

import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SessionInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_session', models.TimeField(verbose_name='Время сеанса')),
                ('places_left', models.IntegerField(default=15, verbose_name='Осталось билетов')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_category', models.CharField(choices=[('K', 'Детский'), ('A', 'Взрослый')], max_length=20, verbose_name='Тип билета')),
                ('ticket_price', models.IntegerField(default=1200, verbose_name='Цена билета')),
                ('tourist_name', models.CharField(max_length=100, verbose_name='Имя туриста')),
                ('tourist_lastname', models.CharField(max_length=100, verbose_name='Фамилия туриста')),
                ('tourist_surname', models.CharField(blank=True, max_length=100, verbose_name='Отчество туриста (опционально)')),
                ('tourist_email', models.EmailField(max_length=254, verbose_name='Электронная почта туриста')),
                ('tourist_country', django_countries.fields.CountryField(max_length=2, verbose_name='Страна проживания туриста')),
            ],
            options={
                'verbose_name': 'Билет',
                'verbose_name_plural': 'Билеты',
            },
        ),
    ]
