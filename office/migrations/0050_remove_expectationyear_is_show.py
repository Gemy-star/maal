# Generated by Django 3.0 on 2022-03-06 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0049_expectationyear_is_show'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expectationyear',
            name='is_show',
        ),
    ]
