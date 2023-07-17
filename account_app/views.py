from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView

from account_app.models import Doctor, Patient, ProfileDoctor, ProfilePatient, ProfileManager, Manager
from content_app.models import Appointment


# DOCTOR
class RegisterDoctor(CreateView):
    """ "view" which is responsible for registering the doctor """

    model = Doctor
    success_url = reverse_lazy('main')
    template_name = 'account_app/doctor_register.html'
    fields = ['username', 'password', 'email', 'specializations', 'exp', 'first_name', 'last_name']


class ProfileDoctorView(ListView):
    """ view which is responsible for displaying the doctor's profile """

    model = ProfileDoctor
    template_name = 'account_app/doctor_profile.html'
    context_object_name = 'doctor_profile'

    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.kwargs.get('username')
        if username is not None:
            queryset = queryset.filter(user__username=username)
        return queryset


class AppointmentGetView(LoginRequiredMixin, ListView):
    """ view which is responsible for displaying doctor's appointments """

    model = Appointment
    template_name = 'account_app/appointment.html'
    context_object_name = 'get_appointment'

    def get_queryset(self):
        doctor_username = self.request.user.username
        return Appointment.objects.filter(user_doctor__username=doctor_username)


# PATIENT
class RegisterPatient(CreateView):
    """ view which is responsible for patient registration """

    model = Patient
    success_url = reverse_lazy('main')
    template_name = 'account_app/patient_register.html'
    fields = ['username', 'password', 'email', 'genders', 'citizenship', 'first_name', 'last_name']


class ProfilePatientView(ListView):
    """ view which is responsible for displaying the patient's profile """

    model = ProfilePatient
    template_name = 'account_app/patient_profile.html'
    context_object_name = 'patient_profile'

    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.kwargs.get('username')
        if username is not None:
            queryset = queryset.filter(user__username=username)
        return queryset


# MANAGER
class ProfileManagerView(ListView):
    """ view which is responsible for displaying the manager's profile """

    model = ProfileManager
    template_name = 'account_app/manager_profile.html'
    context_object_name = 'manager_profile'

    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.kwargs.get('username')
        if username is not None:
            queryset = queryset.filter(user__username=username)
        return queryset


class RegisterManager(CreateView):
    """ "view" which is responsible for registering the manager """

    model = Manager
    success_url = reverse_lazy('main')
    template_name = 'account_app/manager_register.html'
    fields = ['username', 'password', 'email', 'first_name', 'last_name']


class AppointmentGetViewManager(LoginRequiredMixin, ListView):
    """ view that is responsible for outputting all appointment requests """

    model = Appointment
    template_name = 'account_app/appointment_all.html'
    context_object_name = 'get_all_appointment'


def click(request, pk):
    """ view which is responsible for the manager's approval of a request for a doctor's appointment """

    if request.method == 'POST':
        appointment = Appointment.objects.filter(pk=pk)
        appointment.update(click_bool=True)

    return HttpResponseRedirect(reverse('appointment_all', args=[request.user.username]))


class LoginForms(LoginView):
    """ view that is responsible for the authentication """

    redirect_authenticated_user = True
    template_name = 'account_app/login.html'

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValueError("Ваш аккаунт удалён.")
        return reverse_lazy('main')

    def get_success_url(self):
        return reverse_lazy('main')

    def form_invalid(self, form):
        messages.error(self.request, 'хуй')
        return self.render_to_response(self.get_context_data(form=form))


class LogOut(LogoutView):
    """ view that is responsible for logging out """

    template_name = 'account_app/logout.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('login')
