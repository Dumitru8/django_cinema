from django import forms

from .models import Reviews, RatingStar, Rating


class ReviewForm(forms.ModelForm):
    """Reviews form"""

    class Meta:
        model = Reviews
        fields = ('name', 'emails', 'text')


class RatingForm(forms.ModelForm):
    """Add Rating Form"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ('star', )
