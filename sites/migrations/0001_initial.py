# Generated by Django 5.0.1 on 2024-01-09 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('createat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.createat')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('body', models.TextField(verbose_name='Body')),
                ('be_answeraed', models.BooleanField(default=True, verbose_name='Answeraed')),
            ],
            options={
                'verbose_name': 'feedback',
                'verbose_name_plural': 'feedback',
                'db_table': 'feedback',
            },
            bases=('common.createat',),
        ),
        migrations.CreateModel(
            name='PermisionSite',
            fields=[
                ('createat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.createat')),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('permission_url', models.URLField(verbose_name='url')),
                ('image', models.ImageField(upload_to='site/permissions/%Y/%M/%d', verbose_name='image')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
            ],
            options={
                'verbose_name': 'permissions',
                'verbose_name_plural': 'permissions',
                'db_table': 'permissions',
            },
            bases=('common.createat', models.Model),
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=200, unique=True, verbose_name='Site Name')),
                ('site_url', models.URLField(verbose_name='Site URL')),
                ('site_logo', models.ImageField(upload_to='site/logo/%Y/%M/%d', verbose_name='Site Logo')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone')),
                ('landing_phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Landing Phone')),
                ('fax', models.CharField(blank=True, max_length=15, null=True, verbose_name='Fax')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email')),
                ('copy_write', models.TextField(verbose_name='Copy write')),
                ('is_main_setting', models.BooleanField(default=False, verbose_name='Is main setting')),
                ('address', models.TextField(verbose_name='Address')),
                ('abour_us_text', models.TextField(blank=True, null=True, verbose_name='Abour Text')),
            ],
            options={
                'verbose_name': 'site setting',
                'verbose_name_plural': 'site settings',
                'db_table': 'site_settings',
            },
        ),
    ]