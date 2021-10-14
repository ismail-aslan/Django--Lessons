# Generated by Django 3.2.8 on 2021-10-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_relationships', '0002_frameworks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('language', models.ManyToManyField(to='dj_relationships.Languages')),
            ],
        ),
    ]