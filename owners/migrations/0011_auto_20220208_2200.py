# Generated by Django 3.0 on 2022-02-08 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0010_auto_20220201_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companiesarrow',
            name='total_arrows_owned',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='finicalcompaniesarrow',
            name='numberOFArrows',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]