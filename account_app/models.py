from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


# BASE_USER_MODEL
class CustomUser(AbstractUser):
    class Types(models.TextChoices):
        DOC = 'DOCTOR', 'Doctor'
        PAT = 'PATIENT', 'Patient'
        MNG = 'MANAGER', 'Manager'

    type = models.CharField('Type', max_length=50, choices=Types.choices, default=Types.PAT)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='Groups',
        blank=True,
        related_name='custom_user_set'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='User permissions',
        blank=True,
        related_name='custom_user_set'
    )

    def get_absolute_url(self):
        return reverse('user:detail', kwargs={'username': self.username})

    class Meta:
        verbose_name = 'All user'
        verbose_name_plural = 'All users'

    def save(self, *args, **kwargs):
        if not self.is_staff:
            self.set_password(self.password)
        return super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.id}/{self.type} / {self.username}'


# DOCTOR_MODEL
class DoctorManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=CustomUser.Types.DOC)

    def normalize_email(self, email):
        normalized_email = email.lower()
        return normalized_email


class Doctor(CustomUser):
    SPECIALIZATIONS = [
        ('Хирург', 'Хирург'),
        ('Окулист', 'Окулист'),

    ]
    specializations = models.CharField(max_length=55, choices=SPECIALIZATIONS, verbose_name='Специализация',
                                       blank=True)
    exp = models.TextField(default='...', blank=True)
    objects = DoctorManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = CustomUser.Types.DOC
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'


class ProfileDoctor(models.Model):
    user = models.OneToOneField(Doctor, on_delete=models.CASCADE, related_name='doctor_profile')
    avatar = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.id}/ {self.user}'


# PATIENT_MODEL

class PatientManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=CustomUser.Types.PAT)

    def normalize_email(self, email):
        normalized_email = email.lower()
        return normalized_email


class Patient(CustomUser):
    GENDERS = [('m', 'Мужчина'),
               ('f', 'Женщина')]
    CITIZENSHIP = [('RU', 'Россия'),
                   ('BY', 'Белорусь'),
                   ('UK', 'Украина')]

    genders = models.CharField(max_length=1, choices=GENDERS, verbose_name='Пол', blank=True)
    citizenship = models.CharField(max_length=2, choices=CITIZENSHIP, verbose_name='Гражданство', blank=True)

    objects = PatientManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = CustomUser.Types.PAT
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'


class ProfilePatient(models.Model):
    user = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='patient_profile')
    avatar = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.id}/ {self.user}'


class ManagerManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=CustomUser.Types.MNG)

    def normalize_email(self, email):
        normalized_email = email.lower()
        return normalized_email


# MANAGER_MODEL
class Manager(CustomUser):
    objects = ManagerManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = CustomUser.Types.MNG
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'


class ProfileManager(models.Model):
    user = models.OneToOneField(Manager, on_delete=models.CASCADE, related_name='manager_profile')
    avatar = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.id}/ {self.user}'


# automatic profile creation
@receiver(post_save, sender=Doctor)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if isinstance(instance, Doctor):
            ProfileDoctor.objects.create(user=instance)


@receiver(post_save, sender=Patient)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if isinstance(instance, Patient):
            ProfilePatient.objects.create(user=instance)


@receiver(post_save, sender=Manager)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if isinstance(instance, Manager):
            ProfileManager.objects.create(user=instance)
