from django import forms
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

