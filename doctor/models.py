from django.db import models
from django.template.defaultfilters import truncatewords
from django_jalali.db import models as jalali_models
from common.models import CreateAt, UpdateAt
from django.utils.translation import gettext_lazy as _


class Doctor(CreateAt, UpdateAt):
    user = models.OneToOneField('accounts.Users', on_delete=models.PROTECT, related_name='doctor')
    medical_system_code = models.CharField(_('Medical System Code'), max_length=10, unique=True)
    nation_code = models.CharField(_('National Code'), max_length=10, unique=True)
    address_doctor = models.TextField(_('Address'))
    image = models.ImageField(_('Image'), upload_to='doctors/%Y/%M/%d', width_field='with_image', height_field='height_image')
    with_image = models.PositiveIntegerField(editable=False, blank=True, null=True)
    height_image = models.PositiveIntegerField(editable=False, blank=True, null=True)
    doctor_birth_dat = models.DateField(_('Date of Birth milady'), null=True, blank=True)
    doctor_date_shamsi = jalali_models.jDateField(_('Date of Shamsi'), blank=True, null=True)
    is_active = models.BooleanField(_('Is Active'), default=False)
    reply_to = models.TextField(_('Reply to'), null=True, blank=True)
    skill = models.ManyToManyField('SkilDoctor', related_name='doctors')
    about_us_doctor = models.TextField(_('about us doctor'), null=True, blank=True)
    
    class Status(models.TextChoices):
        reject = 'rejected'
        accept = 'accept'
        wating = 'waiting'
    status = models.CharField(_("status send information"), max_length=8, choices=Status.choices, blank=True, null=True)
    
    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
    gender = models.CharField(_('Gender'), max_length=6, choices=Gender.choices)
    
    def __str__(self) -> str:
        return f'{self.user.get_full_name()} -- {self.medical_system_code}'
    
    class Meta:
        db_table = 'doctors'
        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'


class SkilDoctor(CreateAt, UpdateAt):
    skill_name = models.CharField(_("skill doctor"), max_length=50)

    def __str__(self) -> str:
        return self.skill_name
    
    class Meta:
        db_table = 'skil_doctor'
        verbose_name = 'skil_doctor'
        verbose_name_plural = 'skil_doctor'


class ContactUs(CreateAt, UpdateAt):
    title = models.CharField(_('Title'), max_length=100)
    email = models.CharField(_('Email'), max_length=100)
    body = models.TextField(_('Body'))
    reply_to = models.TextField(_('Reply-To'))
    be_answered = models.BooleanField(_('Answered'), default=True)
    
    def __str__(self) -> str:
        return f'{self.title} -- {self.email}'
    
    class Meta:
        db_table = 'contact_us'
        verbose_name = 'contact us'
        verbose_name_plural = 'contact us'


class Communications(CreateAt, UpdateAt):
    address = models.TextField(_("Address"))
    
    class Meta:
        db_table = 'communications'
        verbose_name = 'communication'
        verbose_name_plural = 'communications'


class CommunicationPhone(CreateAt, UpdateAt):
    communication = models.ForeignKey('Communications', on_delete=models.CASCADE, related_name='phones')
    phone = models.CharField(_('Phone'), max_length=15, unique=True)
    
    class Meta:
        db_table = 'communication_phones'
        verbose_name = 'communication phone'
        verbose_name_plural = 'communication phones'


class Faq(CreateAt, UpdateAt):
    title = models.CharField(_('Title'), max_length=100)
    body = models.TextField(_('Body'))
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'faqs'
        verbose_name = 'faq'
        verbose_name_plural = 'faqs'


class QuestionDoctor(CreateAt):
    full_name = models.CharField(_('full name'), max_length=50)
    title = models.CharField(_('title'), max_length=100)
    body = models.TextField(_('body'))
    is_active = models.BooleanField(_('active'), default=False)

    def __str__(self):
        return self.title

    class Mata:
        db_table = 'question_doctor'
        verbose_name = 'question doctor'
        verbose_name_plural = 'question doctor'


class AnswerDoctor(CreateAt, UpdateAt):
    question = models.ForeignKey(QuestionDoctor, on_delete=models.CASCADE, related_name='question')
    body = models.TextField(_('body'))
    is_active = models.BooleanField(_('active'), default=False)

    def __str__(self):
        body_truncate = truncatewords(self.body, 30)
        return f'{self.question.full_name} -- {body_truncate}'

    class Meta:
        db_table = 'answer_doctor'
        verbose_name = 'answer doctor'
        verbose_name_plural = 'answer doctor'


class CardAppointmentDoctor(CreateAt, UpdateAt):
    user = models.ForeignKey('accounts.Users', on_delete=models.CASCADE, related_name='appointments', blank=True,
                             null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments_doctor_admin')
    from_time = jalali_models.jDateTimeField(_('from time'), unique=True)
    at_time = jalali_models.jDateTimeField(_('at time'), unique=True)
    price = models.PositiveIntegerField()
    cancel_description = models.TextField(_('cancel description'), blank=True, null=True)
    status = models.BooleanField(_('status'), default=True)

    def __str__(self):
        return  f'{self.doctor.user.get_full_name} -- {self.from_time} -- {self.at_time}'

    class Meta:
        db_table = 'card_appointment_doctor_admin'
        verbose_name = 'card_appointment_doctor_admin'
        verbose_name_plural = 'card_appointment_doctor_admin'
