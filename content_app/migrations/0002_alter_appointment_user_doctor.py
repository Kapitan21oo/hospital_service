# Generated by Django 4.2.2 on 2023-07-04 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0001_initial'),
        ('content_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='user_doctor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_appointment', to='account_app.doctor'),
        ),
    ]
