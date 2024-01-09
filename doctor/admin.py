from django.contrib import admin
from .models import Doctor, SkilDoctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('doctor_information', {'fields': ('user', 'medical_system_code', 'nation_code', 'doctor_birth_dat', 'skill', 'is_active', 'address_doctor', 'image')}),
        ('reply_to_doctor', {'fields': ('status', "reply_to",)}) 
    ]
    list_display = ('user', 'medical_system_code', 'nation_code', 'doctor_birth_dat', 'is_active', 'skill_doctor', 'status')
    raw_id_fields = ('user',)
    list_filter = ('create_at', 'update_at', 'is_active')
    list_editable = ('is_active', 'status')
    filter_horizontal = ('skill',)
    search_fields = ('user',)
    
    def skill_doctor(self, obj):
        return ','.join([s.skill_name for s in obj.skill.all()])


@admin.register(SkilDoctor)
class SkilDoctorAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'create_at', 'update_at')
    search_fields = ('skill_name',)
    list_filter = ('create_at', 'update_at')