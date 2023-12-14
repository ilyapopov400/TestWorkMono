from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexMono(TemplateView):
    '''
    просмотр главной страницы 'mono/index.html'
    '''
    template_name = 'mono/index.html'
