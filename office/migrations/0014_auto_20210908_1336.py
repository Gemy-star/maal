# Generated by Django 3.0 on 2021-09-08 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0013_auto_20210907_1657'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='rates',
            name='office_rate_FairVal_8397e0_idx',
        ),
        migrations.RemoveField(
            model_name='rates',
            name='AnalayticName',
        ),
        migrations.AddField(
            model_name='rates',
            name='AnalayticName',
            field=models.ManyToManyField(related_name='AnalayticName', to='office.FinicialAnalyst'),
        ),
        migrations.RemoveField(
            model_name='rates',
            name='CompanyEntered',
        ),
        migrations.AddField(
            model_name='rates',
            name='CompanyEntered',
            field=models.ManyToManyField(null=True, related_name='CompanyEntered', to='office.FinicialCompany'),
        ),
        migrations.RemoveField(
            model_name='rates',
            name='ResearchCompany',
        ),
        migrations.AddField(
            model_name='rates',
            name='ResearchCompany',
            field=models.ManyToManyField(null=True, related_name='ResearchCompany', to='office.ResearchCompany'),
        ),
        migrations.AddIndex(
            model_name='rates',
            index=models.Index(fields=['FairValue'], name='office_rate_FairVal_6fb5a4_idx'),
        ),
    ]
