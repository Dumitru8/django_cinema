from django import forms
from .models import Contact
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class ContactForm(forms.ModelForm):
    """email subscription form"""
    email = forms.EmailField(label='', widget=forms.TextInput(
        attrs={'class': 'editContent', 'placeholder': 'Your email...'}
    ))
    captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = ('email', 'captcha')
