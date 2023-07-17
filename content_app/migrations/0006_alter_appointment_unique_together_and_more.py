# Generated by Django 4.2.2 on 2023-07-12 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0005_appointment_time_list'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time_reception',
            field=models.DateField(help_text='Выберите дату и время приема(Форма - ГГГГ-ММ-ДД)'),
        ),
    ]
