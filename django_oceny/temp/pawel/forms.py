from django import forms
from .models import Wpisy

class WpisyForm(forms.ModelForm):
    class Meta:
        model = Wpisy
        fields = ['tytul', 'wpis', 'autor']
