# Generated by Django 2.2 on 2019-06-18 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20190618_2035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rdv',
            old_name='time',
            new_name='rdv_time',
        ),
    ]
