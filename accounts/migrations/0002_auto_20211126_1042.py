# Generated by Django 3.0 on 2021-11-26 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_Client',
            field=models.BooleanField(default=False, help_text='Designates whether this user should be treated as a Client. ', verbose_name='Client'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'ممثل المؤسسة'), (2, 'موظف'), (3, 'عميل')], help_text='User Role in A system ', null=True, verbose_name='User Type'),
        ),
    ]
