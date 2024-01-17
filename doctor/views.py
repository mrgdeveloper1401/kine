from django.shortcuts import render, redirect, get_list_or_404
from django.views import View
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .form import SignUpDoctorForm, QuestionDoctorForm
from .models import Doctor, CardAppointmentDoctor, QuestionDoctor


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
            Doctor.objects.create(user=request.user, **form.cleaned_data)
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


class AdvanceSearchDoctorView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'doctor/advance_search_doctor.html')


class AppointmentDoctorView(View):
    template_name = 'doctor/details_doctor.html'

    def get(self, request, *args, **kwargs):
        details = Doctor.objects.get(id=kwargs['doctor_id'])
        return render(request, self.template_name, {'details': details})


class CardAppointmentView(View):
    template_name = 'doctor/card_appointment.html'

    def get(self, request, *args, **kwargs):
        appointments_user = CardAppointmentDoctor.objects.filter(status=True)
        return render(request, self.template_name, {'appointments_user': appointments_user})


class DetailsQuestionDoctorView(View):
    template_name = 'doctor/details_question_doctor.html'
    form_class = QuestionDoctorForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            QuestionDoctor.objects.create(**form.cleaned_data)
            messages.success(request, 'سوال شما با موفقیت ساخته شد و پس از تایید به مایش در خواهد آمد', 'success')
            return redirect('doctor:order_details_doctor', pk=kwargs['pk'])
        return render(request, self.template_name, {'form': form})
