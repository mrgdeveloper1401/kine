from django.shortcuts import render
from django.views import View
from doctor.models import Doctor, SkilDoctor


class OrderDetailsDoctor(View):
    template_name = 'orders/order_details_doctor.html'

    def get(self, request, *args, **kwargs):
        order_details_doctor = Doctor.objects.get(pk=kwargs['pk'])
        context = {'order_details_doctor': order_details_doctor}
        return render(request, self.template_name, context)
