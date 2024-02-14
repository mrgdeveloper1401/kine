from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


unicode_validator = RegexValidator(
    regex=r'^[a-zA-Z\-\_\s\.]+$',
    message='please enter unicode characters',
    code='invalid characters',
)
    

