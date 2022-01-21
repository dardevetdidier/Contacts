from django import forms

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