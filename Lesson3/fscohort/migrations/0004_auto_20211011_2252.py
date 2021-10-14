# Generated by Django 3.2.8 on 2021-10-11 19:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0003_auto_20211011_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='About_me',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='students',
            name='last_update_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='students',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]