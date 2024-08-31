from django import forms
from .models import Link


class URLForm(forms.ModelForm):
    full_url = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Link
        fields = ('full_url', )
