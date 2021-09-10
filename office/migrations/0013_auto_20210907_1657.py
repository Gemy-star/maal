# Generated by Django 3.0 on 2021-09-07 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0012_auto_20210907_1655'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='companycategory',
            index=models.Index(fields=['name'], name='office_comp_name_0ae9aa_idx'),
        ),
        migrations.AddIndex(
            model_name='companycode',
            index=models.Index(fields=['code', 'company'], name='office_comp_code_27c554_idx'),
        ),
        migrations.AddIndex(
            model_name='finicialcompany',
            index=models.Index(fields=['name', 'category'], name='office_fini_name_4982d4_idx'),
        ),
    ]