from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone

# Create your models here
class SessionInfo(models.Model):
    datetime_of_session = models.DateTimeField(verbose_name="Время сеанса", default=timezone.now)
    places_left = models.IntegerField(verbose_name="Осталось билетов", default=15)

    class Meta:
        verbose_name = "Сеанс"
        verbose_name_plural = "Сеансы"

    def __str__(self):
        return f"Сеанс на время {self.datetime_of_session.hour}:{self.datetime_of_session.minute}"

class Ticket(models.Model):
    ticket_type = (
        ("K", "Детский"),
        ("A", "Взрослый")
    )
    ticket_category = models.CharField(verbose_name="Тип билета", max_length=20, choices=ticket_type)
    ticket_price = models.IntegerField(verbose_name="Цена билета", default=1200)
    tourist_name = models.CharField(verbose_name="Имя туриста", max_length=100)
    tourist_lastname = models.CharField(verbose_name="Фамилия туриста", max_length=100)
    tourist_surname = models.CharField(verbose_name="Отчество туриста (опционально)", max_length=100, blank=True)
    tourist_email = models.EmailField(verbose_name="Электронная почта туриста")
    tourist_country = CountryField(verbose_name="Страна проживания туриста")
    session_datetime = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, verbose_name="Выбранный сеанс")

    class Meta:
        verbose_name = "Билет"
        verbose_name_plural = "Билеты"

    def __str__(self):
        return f"Билет №{self.pk}"