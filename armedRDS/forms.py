from django.forms import ModelForm
from django import forms


from .models import *

class ContactForm(ModelForm): 
    
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "placeholder": "Full Name"
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "placeholder": "Email Address"
    }))


    subject = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "placeholder": "Subject"
    }))


    message = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "type": "text",
        "placeholder": "Why do you want to joine the Armed Forces?"
    }))

    class Meta:
        model = Contact
        fields = ['name','email','subject','message']