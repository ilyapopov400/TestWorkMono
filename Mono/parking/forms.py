from django import forms

from . import models


class CarForm(forms.ModelForm):
    class Meta:
        model = models.Car
        fields = '__all__'
        labels = {
            'brand_car': 'марка',
            'model_car': 'модель',
            'color_car': 'цвет кузова',
            'state_number': 'государственный номер',
            'in_parking': 'статуса автомобиля на стоянке',
            'client': 'владелец автомобиля',
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        exclude = ['cars', ]
        labels = {
            'name': 'ФИО',
            'sex': 'пол',
            'phone': 'телефон',
            'address': 'адрес',
            'cars': 'автотранспорт клиента',
        }
