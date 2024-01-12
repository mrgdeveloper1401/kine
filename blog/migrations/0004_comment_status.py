# Generated by Django 5.0.1 on 2024-01-12 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_categoryblog_level_remove_categoryblog_lft_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.CharField(blank=True, choices=[('published', 'Publish'), ('rejected', 'Rejected'), ('draft', 'Draft')], max_length=9, null=True, verbose_name='Status'),
        ),
    ]