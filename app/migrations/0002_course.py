# Generated by Django 4.1.1 on 2022-09-12 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=255)),
                ('cid', models.CharField(max_length=255)),
                ('totalenrolled', models.CharField(max_length=255)),
            ],
        ),
    ]