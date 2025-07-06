from django import forms
from .models import SuperHeroes

class SuperheroForm(forms.ModelForm):
    class Meta:
        model = SuperHeroes
        fields = ['name', 'alias', 'superpower', 'city', 'active']
