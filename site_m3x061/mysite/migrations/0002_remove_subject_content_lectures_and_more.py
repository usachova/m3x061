# Generated by Django 4.0.4 on 2022-06-29 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='content_lectures',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='content_practice',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='deadlines',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='h1',
        ),
    ]
