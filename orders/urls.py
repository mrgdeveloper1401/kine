from django.urls import path
from .views import OrdersView

app_name = 'orders'
urlpatterns = [
    path('appointments/', OrdersView.as_view(), name='appointments'),
]