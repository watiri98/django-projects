# Generated by Django 2.2.3 on 2019-10-15 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20190610_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, null=True, related_name='students', to='course.Course'),
        ),
    ]
