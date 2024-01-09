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
            name='NewsLater',
            fields=[
                ('createat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.createat')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'News Later',
                'verbose_name_plural': 'News Later',
                'db_table': 'doctor_news_later',
            },
            bases=('common.createat',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('createat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.createat')),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=254, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(allow_unicode=True, max_length=254, unique=True)),
                ('image', models.ImageField(upload_to='blog/%Y/%M/%d', verbose_name='Image')),
                ('width_image', models.PositiveIntegerField(blank=True, null=True)),
                ('height_image', models.PositiveIntegerField(blank=True, null=True)),
                ('body', models.TextField()),
                ('is_active', models.BooleanField(default=False)),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='tiny description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'posts',
                'verbose_name_plural': 'posts',
            },
            bases=('common.createat', models.Model),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('createat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.createat')),
                ('body', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_comments', to=settings.AUTH_USER_MODEL)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='post_comments', to='blog.post')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'db_table': 'comment',
            },
            bases=('common.createat',),
        ),
    ]
