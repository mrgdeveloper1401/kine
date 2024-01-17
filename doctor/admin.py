from django.contrib import admin
from .models import Doctor, SkilDoctor, QuestionDoctor, AnswerDoctor, CardAppointmentDoctor
from django_jalali.admin.filters import JDateFieldListFilter


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('doctor_information', {'fields': ('user', 'medical_system_code', 'nation_code', 'doctor_birth_dat',
                                           'doctor_date_shamsi', 'skill',
                                           'is_active', 'address_doctor', 'image', 'about_us_doctor')}),
        ('reply_to_doctor', {'fields': ('status', "reply_to",)}) 
    ]
    list_display = ('user', 'medical_system_code', 'nation_code', 'doctor_birth_dat', 'is_active', 'skill_doctor',
                    'status')
    raw_id_fields = ('user',)
    list_filter = (('create_at', JDateFieldListFilter), ('update_at', JDateFieldListFilter), 'is_active')
    list_editable = ('is_active', 'status')
    filter_horizontal = ('skill',)
    search_fields = ('user',)
    
    def skill_doctor(self, obj):
        return ','.join([s.skill_name for s in obj.skill.all()])


@admin.register(SkilDoctor)
class SkilDoctorAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'create_at', 'update_at')
    search_fields = ('skill_name',)
    list_filter = (('create_at,', JDateFieldListFilter), ('update_at', JDateFieldListFilter))


@admin.register(QuestionDoctor)
class QuestionDoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'is_active', 'body')
    list_filter = ('is_active', 'create_at', )
    list_per_page = 20
    search_fields = ('body',)
    list_editable = ('is_active', )


@admin.register(AnswerDoctor)
class AnswerDoctorAdmin(admin.ModelAdmin):
    list_display = ('question', 'is_active', 'body')
    raw_id_fields = ('question',)
    list_filter = ('is_active', 'create_at', 'update_at')
    search_fields = ('body',)
    list_per_page = 20
    list_editable = ('is_active', )


# @admin.register(CardAppointment)
# class CardAppointmentAdmin(admin.ModelAdmin):
#     raw_id_fields = ('user', 'doctor')
#     list_display = ('user', 'doctor', 'from_time', 'at_time', 'status')
#     list_filter = ('status', 'at_time', 'from_time', 'create_at', 'update_at')


@admin.register(CardAppointmentDoctor)
class CardAppointmentAdminAdmin(admin.ModelAdmin):
    list_display = ('user', 'doctor', 'from_time', 'at_time', 'status')
    raw_id_fields = ('doctor', 'user')
    list_filter = ('create_at', 'update_at', 'status')
    search_fields = ('doctor',)
    list_per_page = 20
    list_editable = ('status',)