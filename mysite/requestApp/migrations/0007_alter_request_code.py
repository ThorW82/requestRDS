# Generated by Django 4.1.3 on 2022-11-24 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestApp', '0006_alter_request_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='code',
            field=models.CharField(default='1', max_length=23, unique=True, verbose_name='Код'),
        ),
    ]