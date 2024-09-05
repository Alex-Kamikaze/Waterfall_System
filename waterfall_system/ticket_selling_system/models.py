from django.db import models
from django_countries.fields import CountryField

# Create your models here
class SessionInfo(models.Model):
    time_of_session = models.TimeField(verbose_name="Время сеанса")
    places_left = models.IntegerField(verbose_name="Осталось билетов", default=15)

class Ticket(models.Model):
    ticket_type = (
        ("K", "Детский"),
        ("A", "Взрослый")
    )
    ticket_category = models.CharField(verbose_name="Тип билета", choices=ticket_type)
    ticket_price = models.IntegerField(verbose_name="Цена билета", default=1200)
    tourist_name = models.CharField(verbose_name="Имя туриста", max_length=100)
    tourist_lastname = models.CharField(verbose_name="Фамилия туриста", max_length=100)
    tourist_surname = models.CharField(verbose_name="Отчество туриста (опционально)", max_length=100, blank=True)
    tourist_email = models.EmailField(verbose_name="Электронная почта туриста")
    tourist_country = CountryField(verbose_name="Страна проживания туриста")

    class Meta:
        verbose_name = "Билет"
        verbose_name_plural = "Билеты"

    def __str__(self):
        return f"Билет №{self.pk}"