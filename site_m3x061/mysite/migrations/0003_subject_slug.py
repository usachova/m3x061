# Generated by Django 4.0.4 on 2022-07-04 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_remove_subject_content_lectures_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='slug',
            field=models.CharField(default='subject', max_length=25),
        ),
    ]
