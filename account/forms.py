from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput(),max_length=150)

    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]













