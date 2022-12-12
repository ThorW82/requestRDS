# Generated by Django 4.1.3 on 2022-12-08 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_alter_userprofile_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='manager',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='manager',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='userprofile.userprofile', verbose_name='Керівник'),
        ),
    ]
