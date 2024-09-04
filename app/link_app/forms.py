from django import forms
from .models import Link


class URLForm(forms.ModelForm):
    full_url = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'full_url',
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Link
        fields = ('full_url', )
