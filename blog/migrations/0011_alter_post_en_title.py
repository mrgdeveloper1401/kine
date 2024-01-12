# Generated by Django 5.0.1 on 2024-01-12 12:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_en_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='en_title',
            field=models.CharField(max_length=254, unique=True, validators=[django.core.validators.RegexValidator(code='invalid characters', message='please enter unicode characters', regex='^[a-zA-Z\\-\\_]+$'), django.core.validators.MinLengthValidator(20)], verbose_name='en Title'),
        ),
    ]