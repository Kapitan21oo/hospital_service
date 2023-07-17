
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from account_app.models import Doctor, Patient
from content_app.models import Appointment


class DoctorListView(ListView):
    """ view is responsible for displaying all available doctors """

    model = Doctor
    template_name = 'content_app/mainpage.html'
    context_object_name = 'profile_doctor'


class AppointmentView(LoginRequiredMixin, CreateView):
    """ view is responsible for creating a request for a doctor's appointment """

    model = Appointment
    success_url = reverse_lazy('main')
    template_name = 'content_app/appointment.html'
    fields = ['message', 'time_reception', 'time_list']

    def form_valid(self, form):
        doctor_id = self.kwargs['doctor_id']
        doctor = Doctor.objects.get(pk=doctor_id)
        form.instance.user_doctor = doctor
        patient = Patient.objects.get(id=self.request.user.id)
        form.instance.user_patient = patient

        if form.is_valid():
            existing_appointment = Appointment.objects.filter(
                user_doctor=doctor,
                time_reception=form.cleaned_data['time_reception'],
                time_list=form.cleaned_data['time_list']
            ).exists()
            if existing_appointment:
                form.add_error('time_reception', 'Это время занято. Попробуйте выбрать другое время или дату.')
                return self.form_invalid(form)

        return super().form_valid(form)

