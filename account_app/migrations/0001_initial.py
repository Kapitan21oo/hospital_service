# Generated by Django 4.2.2 on 2023-07-04 14:02

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('type', models.CharField(choices=[('DOCTOR', 'Doctor'), ('PATIENT', 'Patient')], default='PATIENT', max_length=50, verbose_name='Type')),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.group', verbose_name='Groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.permission', verbose_name='User permissions')),
            ],
            options={
                'verbose_name': 'All user',
                'verbose_name_plural': 'All users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('specializations', models.CharField(blank=True, choices=[('Хирург', 'Хирург'), ('Окулист', 'Окулист')], max_length=55, verbose_name='Специализация')),
                ('exp', models.TextField(blank=True, default='...')),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctors',
            },
            bases=('account_app.customuser',),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('genders', models.CharField(blank=True, choices=[('m', 'Мужчина'), ('f', 'Женщина')], max_length=1, verbose_name='Пол')),
                ('citizenship', models.CharField(blank=True, choices=[('RU', 'Россия'), ('BY', 'Белорусь'), ('UK', 'Украина')], max_length=2, verbose_name='Гражданство')),
            ],
            options={
                'verbose_name': 'Patient',
                'verbose_name_plural': 'Patients',
            },
            bases=('account_app.customuser',),
        ),
        migrations.CreateModel(
            name='ProfilePatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient_profile', to='account_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_profile', to='account_app.doctor')),
            ],
        ),
    ]
