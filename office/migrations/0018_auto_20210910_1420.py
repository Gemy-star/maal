# Generated by Django 3.0 on 2021-09-10 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0017_auto_20210910_1415'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='rates',
            name='office_rate_FairVal_6fb5a4_idx',
        ),
        migrations.RemoveField(
            model_name='rates',
            name='AnalayticName',
        ),
        migrations.AddField(
            model_name='rates',
            name='AnalayticName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AnalayticName', to='office.FinicialAnalyst'),
        ),
        migrations.RemoveField(
            model_name='rates',
            name='CompanyEntered',
        ),
        migrations.AddField(
            model_name='rates',
            name='CompanyEntered',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CompanyEntered', to='office.FinicialCompany'),
        ),
        migrations.RemoveField(
            model_name='rates',
            name='ResearchCompany',
        ),
        migrations.AddField(
            model_name='rates',
            name='ResearchCompany',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ResearchCompany', to='office.ResearchCompany'),
        ),
        migrations.AddIndex(
            model_name='rates',
            index=models.Index(fields=['FairValue', 'AnalayticName', 'CompanyEntered'], name='office_rate_FairVal_8397e0_idx'),
        ),
    ]
