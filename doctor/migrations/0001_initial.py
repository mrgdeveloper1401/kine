# Generated by Django 5.0.1 on 2024-01-09 14:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Communications',
            fields=[
                ('createat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.createat')),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('address', models.TextField(verbose_name='Address')),
            ],
            options={
                'verbose_name': 'communication',
                'verbose_name_plural': 'communications',
                'db_table': 'communications',
            },
            bases=('common.createat', models.Model),
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('createat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.createat')),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
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
            bases=('common.createat', models.Model),
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('createat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.createat')),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('body', models.TextField(verbose_name='Body')),
            ],
            options={
                'verbose_name': 'faq',
                'verbose_name_plural': 'faqs',
                'db_table': 'faqs',
            },
            bases=('common.createat', models.Model),
        ),
        migrations.CreateModel(
            name='SkilDoctor',
            fields=[
                ('createat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.createat')),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('skill_name', models.CharField(max_length=50, verbose_name='skill doctor')),
            ],
            options={
                'verbose_name': 'skil_doctor',
                'verbose_name_plural': 'skil_doctor',
                'db_table': 'skil_doctor',
            },
            bases=('common.createat', models.Model),
        ),
        migrations.CreateModel(
            name='CommunicationPhone',
            fields=[
                ('createat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.createat')),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('phone', models.CharField(max_length=15, unique=True, verbose_name='Phone')),
                ('communication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='doctor.communications')),
            ],
            options={
                'verbose_name': 'communication phone',
                'verbose_name_plural': 'communication phones',
                'db_table': 'communication_phones',
            },
            bases=('common.createat', models.Model),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('createat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.createat')),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('medical_system_code', models.CharField(max_length=10, unique=True, verbose_name='Medical System Code')),
                ('nation_code', models.CharField(max_length=10, unique=True, verbose_name='National Code')),
                ('address_doctor', models.TextField(verbose_name='Address')),
                ('image', models.ImageField(height_field='height_image', upload_to='doctors/%Y/%M/%d', verbose_name='Image', width_field='with_image')),
                ('with_image', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('height_image', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('doctor_birth_dat', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('reply_to', models.TextField(blank=True, null=True, verbose_name='Reply to')),
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
            bases=('common.createat', models.Model),
        ),
    ]
