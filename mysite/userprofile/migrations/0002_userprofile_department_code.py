# Generated by Django 4.1.3 on 2022-12-06 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='department_code',
            field=models.CharField(blank=True, default=0, max_length=2, null=True),
        ),
    ]
