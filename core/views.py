from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from . import forms
# Create your views here.


class Index(LoginRequiredMixin, generic.TemplateView):
    template_name = "adminlte/index.html"


class Login(generic.FormView):
    template_name = "adminlte/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(
            request=self.request,
            username=username, password=password
        )
        if user is not None:
            login(self.request, user)
        else:
            return super().form_invalid(self, form)
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    pass
