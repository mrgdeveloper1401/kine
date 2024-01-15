from django.shortcuts import render
from django.views.generic import TemplateView


class OrdersView(TemplateView):
    template_name = 'orders/ways_appointements.html'
