from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Contact

CHOICES = [('Amis', 'amis'), ('Famille', 'famille'), ('Travail', 'travail')]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'phone', 'email', 'group']
        choices = CHOICES
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'type',
                'placeholder': 'Prénom Nom',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'type',
                'placeholder': "Téléphone",
            }),
            'email': forms.EmailInput(attrs={
                'class': 'type',
                'placeholder': "Email",
            }),
            'group': forms.Select(attrs={'class': 'type',
                                         'placeholder': 'Groupe'},
                                  choices=CHOICES)
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'type',
                'placeholder': "Nom d'utilisateur",
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'type',
                'placeholder': 'Mot de passe'
            })
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'type',
                'placeholder': "nom d'utilisateur",
            }),
            'email': forms.EmailInput(attrs={
                'class': 'type',
                'placeholder': 'Email',
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'type',
                'placeholder': 'Mot de passe',
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'type',
                'placeholder': 'Confirmer le mot de passe',
            })
        }
