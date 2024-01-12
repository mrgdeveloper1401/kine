# Generated by Django 5.0.1 on 2024-01-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_comment_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-create_at',), 'verbose_name': 'comment', 'verbose_name_plural': 'comments'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('publish', 'Publish'), ('rejected', 'Rejected'), ('draft', 'Draft')], default='draft', max_length=9, verbose_name='Status'),
        ),
    ]
