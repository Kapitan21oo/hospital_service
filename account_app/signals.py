from django.db.models.signals import post_save
from django.dispatch import receiver

from account_app.models import CustomUser, Doctor, ProfileDoctor, ProfilePatient, Patient


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if isinstance(instance, Doctor):
            ProfileDoctor.objects.create(user=instance)
        elif isinstance(instance, Patient):
            ProfilePatient.objects.create(user=instance)
