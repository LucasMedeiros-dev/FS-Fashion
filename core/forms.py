from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    """
    Custom login form with username and password fields.
    """

    username = forms.CharField(
        label="Usuário",
        widget=forms.TextInput(
            attrs={'autofocus': True, 'class': 'form-control'}),
    )

    password = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
