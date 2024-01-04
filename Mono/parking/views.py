from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import FormView

from . import models
from . import forms


# Create your views here.

class ParkingIndex(TemplateView):
    '''
    стартовая страница приложения parking
    '''
    template_name = 'parking/parking-index.html'


class CarsShow(ListView):
    '''
    просмотр всех авто
    '''
    template_name = 'parking/cars-show.html'
    model = models.Car
    context_object_name = 'cars'


class CarWriter(FormView):
    '''
    запись данных о машине
    '''
    form_class = forms.CarForm
    template_name = 'parking/car-writer.html'
    success_url = '/parking/good/'

    def form_valid(self, form):
        form.save()
        return super(CarWriter, self).form_valid(form)


class CarDetail(DetailView, DeleteView):
    '''
    просмотр одного авто
    '''
    template_name = 'parking/car-detail.html'
    model = models.Car
    context_object_name = 'automobile'
    success_url = '/parking/good/'


class ClientsShow(ListView):
    '''
    просмотр всех клиентов
    '''
    template_name = 'parking/clients-show.html'
    model = models.Client
    context_object_name = 'clients'


class ClientWriter(FormView):
    '''
    запись данных о клиенте
    '''
    form_class = forms.ClientForm
    template_name = 'parking/client-writer.html'
    success_url = '/parking/good/'

    def form_valid(self, form):
        form.save()
        return super(ClientWriter, self).form_valid(form)


class ClientDetail(DetailView, DeleteView):
    '''
    просмотр одного клиента
    '''
    template_name = 'parking/client-detail.html'
    model = models.Client
    context_object_name = 'client'
    success_url = '/parking/good/'

    def _get_all_cars(self) -> list:
        '''
        :return: список автомашин клинта
        '''
        client = self.object
        cars = models.Car.objects.filter(client=client)
        return cars

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['all_cars'] = self._get_all_cars()  # список автомашин клинта
        return self.render_to_response(context)


class GoodWriter(TemplateView):
    '''
    просмотр страницы, что действие выполнено успешно
    '''
    template_name = 'parking/good-writer.html'
