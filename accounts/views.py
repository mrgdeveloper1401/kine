from typing import Any
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from random import randint
from .models import Users, OtpCode
from .form import SignUpForm, LoginForm, AcceptCodeForm, PasswordResetForms, EditProfile
from kine.utils import send_code_email


class UserSignupView(View):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('doctor:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next')
        return super().setup(request, *args, **kwargs)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            random_number = randint(1000000, 9999999)
            send_code_email(cd['email'], random_number)
            OtpCode.objects.create(email=cd['email'], code=random_number)
            request.session['user_signup_info'] = {
                'email': cd['email'],
                'username': cd['username'],
                'password': cd['password']
            }
            messages.success(request, 'created account successfully please enter code for active accounts', 'success')
            return redirect('accounts:accept_code')
        return render(request, self.template_name, {'form': form})


class AcceptCodeView(View):
    form_class = AcceptCodeForm
    template_name = 'accounts/accept_code.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        user_session = request.session['user_signup_info']
        otp_code = OtpCode.objects.get(email=user_session['email'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if int(cd['code']) == otp_code.code:
                Users.objects.create_user(
                    email=user_session['email'],
                    password=user_session['password'],
                    username=user_session['username']
                )
                del user_session
                otp_code.delete()
                messages.success(request, 'you have successfully verify accounts', 'success')
                return redirect('accounts:login')
            else:
                messages.error(request, 'your code is invalid', 'danger')
                return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})


class LoginViews(View):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('accounts:profile', request.user.id)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'login successful', 'success')
                return redirect('accounts:profile', request.user.id)
            messages.error(request, 'login failed', 'danger')
        return render(request, self.template_name, {'form': form})


class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'


class LogOutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'successfly logout request', 'success')
        return redirect('accounts:login')


class UserPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'
    form_class = PasswordResetForms


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(Users, pk=kwargs['pk'])
        return render(request, 'accounts/profile.html', {'profile': profile})


class EditProfileView(LoginRequiredMixin, View):
    form_class = EditProfile
    template_name = 'accounts/edit_profile.html'

    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:
        self.user_instance = get_object_or_404(Users, pk=kwargs['pk'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        user = self.user_instance
        form = self.form_class(instance=user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        user = self.user_instance
        form = self.form_class(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully update profile', 'success')
            return redirect('accounts:profile', pk=request.user.id)
        return render(request, self.template_name, {'form': form})
