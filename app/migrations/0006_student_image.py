# Generated by Django 4.1.1 on 2022-09-15 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_course_estatus_student_estatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='blog/app/media/posts'),
        ),
    ]
