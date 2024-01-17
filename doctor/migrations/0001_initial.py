# Generated by Django 5.0.1 on 2024-01-17 15:01

import django.db.models.deletion
import django_jalali.db.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Communications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True)),
                ('update_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('address', models.TextField(verbose_name='Address')),
            ],
            options={
                'verbose_name': 'communication',
                'verbose_name_plural': 'communications',
                'db_table': 'communications',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True)),
                ('update_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('body', models.TextField(verbose_name='Body')),
                ('reply_to', models.TextField(verbose_name='Reply-To')),
                ('be_answered', models.BooleanField(default=True, verbose_name='Answered')),
            ],
            options={
                'verbose_name': 'contact us',
                'verbose_name_plural': 'contact us',
                'db_table': 'contact_us',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True)),
                ('update_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('body', models.TextField(verbose_name='Body')),
            ],
            options={
                'verbose_name': 'faq',
                'verbose_name_plural': 'faqs',
                'db_table': 'faqs',
            },
        ),
        migrations.CreateModel(
            name='QuestionDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True)),
                ('full_name', models.CharField(max_length=50, verbose_name='full name')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('body', models.TextField(verbose_name='body')),
                ('is_active', models.BooleanField(default=False, verbose_name='active')),
            ],
            options={
                'verbose_name': 'create_at',
                'verbose_name_plural': 'create_at',
                'db_table': 'create_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SkilDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True)),
                ('update_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('skill_name', models.CharField(max_length=50, verbose_name='skill doctor')),
            ],
            options={
                'verbose_name': 'skil_doctor',
                'verbose_name_plural': 'skil_doctor',
                'db_table': 'skil_doctor',
            },
        ),
        migrations.CreateModel(
            name='CommunicationPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True)),
                ('update_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('phone', models.CharField(max_length=15, unique=True, verbose_name='Phone')),
                ('communication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='doctor.communications')),
            ],
            options={
                'verbose_name': 'communication phone',
                'verbose_name_plural': 'communication phones',
                'db_table': 'communication_phones',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True)),
                ('update_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('medical_system_code', models.CharField(max_length=10, unique=True, verbose_name='Medical System Code')),
                ('nation_code', models.CharField(max_length=10, unique=True, verbose_name='National Code')),
                ('address_doctor', models.TextField(verbose_name='Address')),
                ('image', models.ImageField(height_field='height_image', upload_to='doctors/%Y/%M/%d', verbose_name='Image', width_field='with_image')),
                ('with_image', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('height_image', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('doctor_birth_dat', models.DateField(blank=True, null=True, verbose_name='Date of Birth milady')),
                ('doctor_date_shamsi', django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='Date of Shamsi')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('reply_to', models.TextField(blank=True, null=True, verbose_name='Reply to')),
                ('about_us_doctor', models.TextField(blank=True, null=True, verbose_name='about us doctor')),
                ('status', models.CharField(blank=True, choices=[('rejected', 'Reject'), ('accept', 'Accept'), ('waiting', 'Wating')], max_length=8, null=True, verbose_name='status send information')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6, verbose_name='Gender')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='doctor', to=settings.AUTH_USER_MODEL)),
                ('skill', models.ManyToManyField(related_name='doctors', to='doctor.skildoctor')),
            ],
            options={
                'verbose_name': 'doctor',
                'verbose_name_plural': 'doctors',
                'db_table': 'doctors',
            },
        ),
        migrations.CreateModel(
            name='CardAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True)),
                ('update_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('from_time', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='from time')),
                ('at_time', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='at time')),
                ('status', models.BooleanField(default=False, verbose_name='status')),
                ('cancel_description', models.TextField(blank=True, null=True, verbose_name='cancel description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments_user', to=settings.AUTH_USER_MODEL)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments_doctor', to='doctor.doctor')),
            ],
            options={
                'verbose_name': 'card_appointment',
                'verbose_name_plural': 'card_appointments',
                'db_table': 'card_appointment',
            },
        ),
        migrations.CreateModel(
            name='AnswerDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True)),
                ('update_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('body', models.TextField(verbose_name='body')),
                ('is_active', models.BooleanField(default=False, verbose_name='active')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='doctor.questiondoctor')),
            ],
            options={
                'verbose_name': 'answer doctor',
                'verbose_name_plural': 'answer doctor',
                'db_table': 'answer_doctor',
            },
        ),
    ]
