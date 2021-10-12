# Generated by Django 3.0 on 2021-10-05 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0027_finicialcompany_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='earningsforecast',
            old_name='expectvalue',
            new_name='realEarn',
        ),
        migrations.RemoveField(
            model_name='earningsforecast',
            name='expectYear',
        ),
        migrations.AddField(
            model_name='earningsforecast',
            name='second2020',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='earningsforecast',
            name='third2020',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='earningsforecast',
            name='total_earn',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]