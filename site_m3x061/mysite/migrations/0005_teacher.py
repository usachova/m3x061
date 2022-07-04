# Generated by Django 4.0.4 on 2022-07-04 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_student_remove_subject_lector_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('patronymic', models.CharField(blank=True, max_length=200, null=True)),
                ('isu', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
