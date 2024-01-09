from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views import View
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from .form import FeedbackForm
from .models import Feedback, SiteSettings, PermisionSite, AboutUs, SciolAboutUs



class contactUsView(View):
    template_name = 'sites/contact_us.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class HeaderComponenets(View):
    template_name = 'sites/header.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class FooterComponents(View):
    template_name = 'sites/footer.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class FeedbackView(View):
    form_class = FeedbackForm
    template_name = 'sites/feedback.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            Feedback.objects.create(**form.cleaned_data)
            messages.success(request, 'tnx your feedback', 'success')
            return redirect('sites:contact_us')
        return render(request, self.template_name, {'form': form})


class LogoDescriptionFooterComponents(View):
    def get(self, request, *args, **kwargs):
        logo_desc_foot = get_object_or_404(SiteSettings, is_main_setting=True)
        return render(request, 'sites/logo_description_footer.html', {'logo_desc_foot': logo_desc_foot})


class ENemadView(View):
    def get(self, request, *args, **kwargs):
        e_nemad = get_list_or_404(PermisionSite, is_active=True)
        return render(request, 'sites/e_nemad.html', {'e_nemad': e_nemad})


class WaysOfComunicarion(View):
    def get(self, request, *args, **kwargs):
        woc = get_object_or_404(SiteSettings, is_main_setting=True)
        return render(request, 'sites/woc.html', {'woc': woc})



class SliderComponenets(TemplateView):
    template_name = 'sites/slider.html'


class AboutUsView(ListView):
    model = AboutUs
    template_name = 'sites/about_us.html'
    context_object_name = 'about_us'
    queryset = get_object_or_404(AboutUs, is_active=True)


class SciolAboutUsView(ListView):
    model = SciolAboutUs
    queryset = get_object_or_404(SciolAboutUs, is_active=True)
    template_name = 'sites/sciol_about_us.html'
    context_object_name = 'sciol_about_us'