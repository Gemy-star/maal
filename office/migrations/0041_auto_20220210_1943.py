# Generated by Django 3.0 on 2022-02-10 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0040_auto_20220210_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finicialcompany',
            name='total_arrows',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
