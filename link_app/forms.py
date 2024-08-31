from django import forms


class URLForm(forms.Form):
    full_url = forms.CharField(widget=forms.TextInput())
