# Generated by Django 3.2.14 on 2022-11-10 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HrEntry', '0003_jobapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblist',
            name='Experiance',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='joblist',
            name='WorkLocation',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
