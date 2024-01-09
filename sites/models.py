from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import CreateAt, UpdateAt


class SiteSettings(models.Model):
    site_name = models.CharField(_('Site Name'), max_length=200, unique=True)
    site_url = models.URLField(_('Site URL'), max_length=200)
    site_logo = models.ImageField(_('Site Logo'), upload_to='site/logo/%Y/%M/%d')
    phone = models.CharField(_('Phone'), max_length=15, blank=True, null=True)
    landing_phone = models.CharField(_('Landing Phone'), max_length=15, blank=True, null=True)
    fax = models.CharField(_('Fax'), max_length=15, blank=True, null=True)
    email = models.EmailField(_('Email'), max_length=100, blank=True, null=True)
    copy_write = models.TextField(_('Copy write'))
    is_main_setting = models.BooleanField(_('Is main setting'), default=False)
    address = models.TextField(_('Address'))
    abour_us_text = models.TextField(_('Abour Text'), blank=True, null=True)
    
    def __str__(self) -> str:
        return self.site_name
    
    class Meta:
        db_table = 'site_settings'
        verbose_name = 'site setting'
        verbose_name_plural = 'site settings'


class Feedback(CreateAt):
    title = models.CharField(_("Title"), max_length=100)
    email = models.EmailField(_("Email"), max_length=100)
    body = models.TextField(_("Body"))
    be_answeraed = models.BooleanField(_("Answeraed"), default=True)
    
    def __str__(self) -> str:
        return f'{self.title} -- {self.email} -- {self.be_answeraed}'
    
    class Meta:
        db_table = 'feedback'
        verbose_name = _('feedback')
        verbose_name_plural = _('feedback')


class PermisionSite(CreateAt, UpdateAt):
    permission_url = models.URLField(_("url"), max_length=200)
    image = models.ImageField(_("image"), upload_to='site/permissions/%Y/%M/%d')
    is_active  = models.BooleanField(_("is_active"), default=True)
    
    class Meta:
        db_table = 'permissions'
        verbose_name = _('permissions')
        verbose_name_plural = _('permissions')