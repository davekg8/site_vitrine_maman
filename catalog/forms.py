# my_app/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Votre Nom", max_length=100,
                           widget=forms.TextInput(attrs={
                               'placeholder': 'Nom Complet',
                               'class': 'input input-bordered w-full focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500'
                           }))
    email = forms.EmailField(label="Votre Email",
                             widget=forms.EmailInput(attrs={
                                 'placeholder': 'email@example.com',
                                 'class': 'input input-bordered w-full focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500'
                             }))
    subject = forms.CharField(label="Sujet", max_length=200,
                              widget=forms.TextInput(attrs={
                                  'placeholder': 'Comment pouvons-nous vous aider ?',
                                  'class': 'input input-bordered w-full focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500'
                              }))
    message = forms.CharField(label="Votre Message", widget=forms.Textarea(attrs={
                                 'placeholder': 'Dites-nous ce dont vous avez besoin...',
                                 'rows': 6, # daisyUI textarea class includes h-32, but rows can be a fallback
                                 'class': 'textarea textarea-bordered w-full h-32 focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500'
                             }))