from django.urls import path
from . import views

urlpatterns = [
    path('', views.ParkingIndex.as_view(), name='parking-index'),  # просмотр главной страницы
    path('carwriter/', views.CarWriter.as_view(), name='car-writer'),  # запись данных об авто
    path('cars/', views.CarsShow.as_view(), name='cars-show'),  # просмотр всех авто
    path('cars/<int:pk>', views.CarDetail.as_view(), name='car-detail'),  # просмотр одного авто
    path('clients/', views.ClientsShow.as_view(), name='clients-show'),  # просмотр всех клиентов
    path('clientwriter/', views.ClientWriter.as_view(), name='client-writer'),  # запись данных о клиенте
    path('clients/<int:pk>', views.ClientDetail.as_view(), name='clients-detail'),  # просмотр одного клиента
    path('good/', views.GoodWriter.as_view(), name='good-writer'),  # указание на успешность действия
]
