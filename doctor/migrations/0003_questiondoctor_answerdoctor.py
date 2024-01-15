# Generated by Django 5.0.1 on 2024-01-15 09:45

import django.db.models.deletion
import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_createat_create_at'),
        ('doctor', '0002_doctor_about_us_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionDoctor',
            fields=[
                ('createat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.createat')),
                ('full_name', models.CharField(max_length=50, verbose_name='full name')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('body', models.TextField(verbose_name='body')),
                ('is_active', models.BooleanField(default=False, verbose_name='active')),
            ],
            bases=('common.createat',),
        ),
        migrations.CreateModel(
            name='AnswerDoctor',
            fields=[
                ('createat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.createat')),
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
            bases=('common.createat', models.Model),
        ),
    ]
