# Generated by Django 2.2.1 on 2019-06-10 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_teacher_upload_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='upload_pic',
        ),
    ]
