from django.urls import path
from .views import RegisterDoctor, RegisterPatient, ProfileDoctorView, LoginForms, ProfilePatientView, LogOut, \
    AppointmentGetView, AppointmentGetViewManager, ProfileManagerView, RegisterManager, click

urlpatterns = [
    path('doctor_register/', RegisterDoctor.as_view(), name='doctor_register'),
    path('patient_register/', RegisterPatient.as_view(), name='patient_register'),
    path('manager_register/', RegisterManager.as_view(), name='patient_register'),


    path('profile/doctor/<str:username>', ProfileDoctorView.as_view(), name='doc_profile'),
    path('profile/manager/<str:username>', ProfileManagerView.as_view(), name='mng_profile'),
    path('profile/patient/<str:username>', ProfilePatientView.as_view(), name='pat_profile'),


    path('appointment/<str:username>', AppointmentGetView.as_view(), name='appointment'),
    path('appointment_all/<str:username>', AppointmentGetViewManager.as_view(), name='appointment_all'),
    path('click/<int:pk>/', click, name='click_bool'),


    path('login', LoginForms.as_view(), name='login'),
    path('logout', LogOut.as_view(), name='logout')
]
