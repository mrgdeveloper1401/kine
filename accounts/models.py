from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.validators import UnicodeUsernameValidator
from .managers import UserManager, SoftDeleteManager
from common.models import CreateAt, UpdateAt


class Users(AbstractBaseUser, PermissionsMixin, UpdateAt, CreateAt):
    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=100)
    email = models.EmailField(_('Email Address'), unique=True)
    is_active = models.BooleanField(_('Active'), default=False)
    is_staff = models.BooleanField(_('Staff'), default=False)
    is_deleted = models.BooleanField(_('delete user'), editable=False, default=False)
    deleted_at = models.DateTimeField(_('deleted at'), editable=False, blank=True, null=True)
    random_active_code = models.CharField(_('random active code'), max_length=72, blank=True, null=True, editable=False)
    image = models.ImageField(_('image'), upload_to='images/user/%Y/%M/%d', width_field='width_image', height_field='height_image', blank=True, null=True)
    width_image = models.IntegerField(_('width'), blank=True, null=True)
    height_image = models.IntegerField(_('height'), blank=True, null=True)
    about_us = models.TextField(_('about us'), blank=True, null=True)
    
    username_validator = UnicodeUsernameValidator()
    
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    objects = UserManager()
    soft_delete_manager = SoftDeleteManager()
    
    def __str__(self) -> str:
        return self.get_full_name()
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
    
    
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class UserDelete(Users):
    class Meta:
        proxy = True
        auto_created = True


class Notofication(CreateAt):
    title = models.CharField(_('Title'), max_length=100)
    body = models.TextField(_('Body'))
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'notifications'
        verbose_name = 'notification'
        verbose_name_plural = 'notifications'


class OtpCode(CreateAt):
    code = models.PositiveIntegerField()
    email = models.EmailField(_('Email'))
    
    def __str__(self) -> str:
        return f'{self.code} - {self.email} - {self.create_at}'
    
    class Meta:
        db_table = 'otp_codes'
        verbose_name = 'otp code'
        verbose_name_plural = 'otp code'