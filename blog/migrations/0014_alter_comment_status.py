# Generated by Django 5.0.1 on 2024-01-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_remove_post_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('pb', 'published'), ('rj', 'rejected'), ('df', 'draft')], default='df', max_length=2),
        ),
    ]
