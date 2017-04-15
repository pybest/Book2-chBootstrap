from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

# Create your views here.

#--- TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'

#--- Class-Based Views for authentication
class UserLoginView(LoginView):
    template_name = 'auth/login.html'

class UserLogoutView(LogoutView):
    template_name = 'auth/logged_out.html'

class UserPasswordChangeView(PasswordChangeView):
    template_name = 'auth/password_change_form.html'

class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'auth/password_change_done.html'

#--- User Creation
class UserCreateView(CreateView):
    template_name = 'auth/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'auth/register_done.html'
