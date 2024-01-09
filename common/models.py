from django.db import models
from django.utils.translation import gettext_lazy as _


class CreateAt(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    
    class Meta:
        
        db_table = 'create_at'
        verbose_name = _('create_at')
        verbose_name_plural = _('create_at')


class UpdateAt(models.Model):
    update_at = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True)
    
    class Meta:
        abstract = True
        db_table = 'update_at'
        verbose_name = _('update_at')
        verbose_name_plural = _('update_at')

    