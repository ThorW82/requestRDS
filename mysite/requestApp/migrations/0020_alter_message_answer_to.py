# Generated by Django 4.1.3 on 2022-12-02 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requestApp', '0019_alter_message_answer_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='answer_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='requestApp.message'),
        ),
    ]