from django.shortcuts import render, redirect, get_list_or_404
from django.views import View
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .form import SignUpDoctorForm
from .models import Doctor
    

class HomeComponents(TemplateView):
    template_name = 'doctor/home.html'


class SignUpDoctorView(LoginRequiredMixin, View):
    from_class = SignUpDoctorForm
    template_name = 'doctor/signup_doctor.html'
    
    def get(self, request, *args, **kwargs):
        form = self.from_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.from_class(request.POST, request.FILES)
        if form.is_valid():
            Doctor.objects.create(user = request.user, **form.cleaned_data)
            messages.success(request, 'send information about you we called', 'success')
            return redirect('accounts:profile', request.user.id)
        return render(request, self.template_name, {'form': form})


class All_doctor(View):
    def get(self, request, *args, **kwargs):
        doctor = Doctor.objects.filter(is_active=True)
        return render(request, 'doctor/all_doctor.html', {'doctor': doctor})


class DoctorSlider(View):
    def get(self, request, *args, **kwargs):
        doctor = get_list_or_404(Doctor, is_active=True)[:10]
        doctor = Doctor.objects.filter(is_active=True)[:10]
        return render(request, 'doctor/doctor_slider.html', {'doctor': doctor})
    

class LatesDoctor(View):
    def get(self, request, *args, **kwargs):
        latest_doctor = Doctor.objects.filter(is_active=True)[:4]
        return render(request, 'doctor/latest_doctor.html', {'latest_doctor': latest_doctor})