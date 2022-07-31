from django import forms
from .models import URLShorten

class URLForm(forms.ModelForm):
    class Meta:
        model = URLShorten
        fields = ['url']
