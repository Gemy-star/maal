# Generated by Django 3.0 on 2021-08-24 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FinicialAnalyst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('CurrentJob', models.CharField(blank=True, max_length=255, null=True)),
                ('pervJob', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('tiwtterAccount', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinicialCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Recommendation', models.CharField(blank=True, max_length=255, null=True)),
                ('FairValue', models.FloatField(blank=True, null=True)),
                ('CurrenncyValue', models.FloatField(blank=True, null=True)),
                ('MarketValue', models.FloatField(blank=True, null=True)),
                ('RecommendDate', models.DateField(auto_now_add=True, null=True)),
                ('report', models.FileField(null=True, upload_to='reportspdf/')),
                ('AnalayticName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AnalayticName', to='office.FinicialAnalyst')),
                ('CompanyEntered', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CompanyEntered', to='office.FinicialCompany')),
                ('EmpEntered', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ResearchCompany', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ResearchCompany', to='office.FinicialCompany')),
            ],
        ),
        migrations.AddField(
            model_name='finicialanalyst',
            name='currentCompany',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='currentCompany', to='office.FinicialCompany'),
        ),
        migrations.AddField(
            model_name='finicialanalyst',
            name='pervCompany',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pervCompany', to='office.FinicialCompany'),
        ),
        migrations.CreateModel(
            name='CompanyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='office.FinicialCompany')),
            ],
        ),
    ]
