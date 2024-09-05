from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "floatingUsername",
            }
        ),
    )
    password = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-2", "id": "floatingPassword"}
        ),
    )
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ["username", "password", "remember_me"]


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-2",
                "id": "floatingUsername",
                "placeholder": "Логин",
            }
        ),
    )
    password1 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mb-2",
                "id": "floatingPassword1",
                "placeholder": "Пароль",
            }
        ),
    )
    password2 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mb-2",
                "id": "floatingPassword2",
                "placeholder": "Подтвердите пароль",
            }
        ),
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
