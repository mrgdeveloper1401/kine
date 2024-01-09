from django.contrib import admin
from .models import SiteSettings, Feedback, PermisionSite


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    pass


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'be_answeraed')
    list_filter = ('create_at', )
    date_hierarchy = 'create_at'


@admin.register(PermisionSite)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('permission_url','create_at', 'update_at', 'is_active')
    list_filter =('create_at', 'update_at', 'is_active')
    date_hierarchy = 'create_at'
    