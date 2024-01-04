from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.

class Client(models.Model):
    CHOICES = (('male', 'Мужской пол'), ('female', 'Женский пол'))

    name = models.CharField(max_length=20, verbose_name="ФИО", blank=False,
                            validators=[MinLengthValidator(3)])  # обязательный, мин 3 символа
    sex = models.CharField(verbose_name="Выберите пол", choices=CHOICES, default="Мужской пол", max_length=40,
                           blank=False)  # обязательный

    phone = models.CharField(max_length=20, verbose_name="телефон", blank=False,
                             unique=True)  # обязательный, уникальный
    address = models.CharField(max_length=20, verbose_name="адрес", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Car(models.Model):
    brand_car = models.CharField(max_length=20, verbose_name="марка", blank=False)  # обязательный
    model_car = models.CharField(max_length=20, verbose_name="модель", blank=False)  # обязательный
    color_car = models.CharField(max_length=20, verbose_name="цвет кузова", blank=False)  # обязательный
    state_number = models.CharField(max_length=20, verbose_name="государственный номер", blank=False,
                                    unique=True)  # обязательный, уникальный
    in_parking = models.BooleanField(blank=False, verbose_name="статуса автомобиля на стоянке")  # обязательный
    client = models.ForeignKey(Client, blank=True, on_delete=models.PROTECT, verbose_name="владелец автомобиля")

    def __str__(self):
        return f"{self.brand_car}/{self.model_car}"
