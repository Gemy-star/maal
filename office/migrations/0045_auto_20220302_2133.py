# Generated by Django 3.0 on 2022-03-02 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0044_auto_20220222_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='earningsforecast',
            name='first_quarter',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='earningsforecast',
            name='fourth_quarter',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]