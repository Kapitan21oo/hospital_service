
from django.urls import path
from .views import DoctorListView, AppointmentView

urlpatterns = [
    path('main/', DoctorListView.as_view(), name='main'),
    path('appointment/<int:doctor_id>', AppointmentView.as_view(), name='appointment')
]
