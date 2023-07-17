# Generated by Django 4.2.2 on 2023-07-12 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Manager',
                'verbose_name_plural': 'Managers',
            },
            bases=('account_app.customuser',),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='type',
            field=models.CharField(choices=[('DOCTOR', 'Doctor'), ('PATIENT', 'Patient'), ('MANAGER', 'Manager')], default='PATIENT', max_length=50, verbose_name='Type'),
        ),
        migrations.CreateModel(
            name='ProfileManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='manager_profile', to='account_app.manager')),
            ],
        ),
    ]