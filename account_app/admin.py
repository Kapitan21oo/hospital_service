from django.contrib import admin

from account_app.models import Doctor, Patient, ProfileDoctor, ProfilePatient, CustomUser, Manager, ProfileManager

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(ProfileDoctor)
admin.site.register(ProfilePatient)
admin.site.register(CustomUser)
admin.site.register(Manager)
admin.site.register(ProfileManager)