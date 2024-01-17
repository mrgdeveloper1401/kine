from django.urls import path
from .views import OrderDetailsDoctor


app_name = 'orders'
urlpatterns = [
    path('order_details_doctor/<int:pk>/', OrderDetailsDoctor.as_view(), name='order_details_doctor')
]