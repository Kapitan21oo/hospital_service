# Generated by Django 4.2.2 on 2023-07-10 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0004_remove_appointment_limit_appointment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='time_list',
            field=models.IntegerField(choices=[(0, '9:00 - 9:30'), (1, '9:30 - 10:00'), (2, '10:00 - 10:30'), (3, '10:30 - 11:00'), (4, '11:00 - 11:30'), (5, '11:30 - 12:00'), (6, '12:00 - 12:30'), (7, '12:30 - 13:00'), (8, '13:00 - 13:30'), (9, '14:30 - 15:00'), (10, '15:00 - 15:30'), (11, '15:30 - 16:00'), (12, '16:00 - 16:30'), (13, '16:30 - 17:00')], default=0),
        ),
    ]
