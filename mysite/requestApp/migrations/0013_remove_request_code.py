# Generated by Django 4.1.3 on 2022-11-30 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestApp', '0012_alter_request_pay_date_alter_request_req_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='code',
        ),
    ]