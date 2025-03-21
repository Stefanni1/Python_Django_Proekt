from django import forms
from .models import Ad

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'category', 'currency', 'image']
        widgets = {
            'category': forms.Select(),
            'currency': forms.Select(),
        }