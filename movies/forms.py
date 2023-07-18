from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import Reviews, RatingStar, Rating


class ReviewForm(forms.ModelForm):
    """Reviews form"""

    captcha = ReCaptchaField()
    class Meta:
        model = Reviews
        fields = ('name', 'emails', 'text', 'captcha')
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border"}),
            "emails": forms.EmailInput(attrs={"class": "form-control border"}),
            "text": forms.Textarea(attrs={"class": "form-control border"}),
        }


class RatingForm(forms.ModelForm):
    """Add Rating Form"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ('star', )
