from django.core.exceptions import ValidationError
from django.db import models

from account_app.models import Doctor, Patient


class Appointment(models.Model):
    TIME_LIST = [(0, '9:00 - 9:30'),
                 (1, '9:30 - 10:00'),
                 (2, '10:00 - 10:30'),
                 (3, '10:30 - 11:00'),
                 (4, '11:00 - 11:30'),
                 (5, '11:30 - 12:00'),
                 (6, '12:00 - 12:30'),
                 (7, '12:30 - 13:00'),
                 (8, '13:00 - 13:30'),
                 (9, '14:30 - 15:00'),
                 (10, '15:00 - 15:30'),
                 (11, '15:30 - 16:00'),
                 (12, '16:00 - 16:30'),
                 (13, '16:30 - 17:00'),
                 ]
    user_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_appointment',
                                    default=None)
    user_patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_appointment',
                                     default=None)
    message = models.TextField(default='...')
    time_reception = models.DateField(help_text='Выберите дату и время приема(Форма - ГГГГ-ММ-ДД)')
    time_list = models.IntegerField(choices=TIME_LIST, default=0)
    click_bool = models.BooleanField(default=False)




    #
    # class Meta:
    #     unique_together = ['user_doctor', 'user_patient']

