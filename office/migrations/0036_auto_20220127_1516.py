# Generated by Django 3.0 on 2022-01-27 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0035_auto_20220126_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rates',
            name='RecommendDate',
            field=models.DateField(null=True),
        ),
    ]