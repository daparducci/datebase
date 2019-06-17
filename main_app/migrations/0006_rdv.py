# Generated by Django 2.2 on 2019-06-16 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20190615_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rdv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('what', models.TextField(blank=True)),
                ('where', models.TextField(blank=True)),
                ('cancel', models.BooleanField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Match')),
            ],
        ),
    ]