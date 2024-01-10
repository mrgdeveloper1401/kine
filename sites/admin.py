from django.contrib import admin
from .models import SiteSettings, Feedback, PermisionSite, AboutUs, SciolAboutUs
from django_jalali.admin.filters import JDateFieldListFilter


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
    list_filter =(('create_at', JDateFieldListFilter), ('update_at', JDateFieldListFilter), 'is_active')
    date_hierarchy = 'create_at'


@admin.register(AboutUs)
class AboutUs(admin.ModelAdmin):
    list_display = ('title', 'image')


@admin.register(SciolAboutUs)
class SciolAboutUs(admin.ModelAdmin):
    list_display = ('title', 'url', 'is_active')
    list_editable= ('is_active',)
    date_hierarchy = 'create_at'
    list_filter = ('is_active',( 'create_at', JDateFieldListFilter), ('update_at', JDateFieldListFilter))
    