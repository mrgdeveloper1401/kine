from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string

def send_code_email(email, code):
    pass


def send_email(subject, to, contact, template_name):
    pass