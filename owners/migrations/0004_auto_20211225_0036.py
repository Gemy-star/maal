# Generated by Django 3.0 on 2021-12-24 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0003_delete_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='companiesarrow',
            name='arrowPrice',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companiesarrow',
            name='ownRatio',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
