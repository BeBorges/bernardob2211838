from django import forms
from .models import Curiosity, TopScorer

class CuriosityForm(forms.ModelForm):
    class Meta:
        model = Curiosity
        fields = ['title', 'info_1', 'info_2', 'info_3']

class TopScorerForm(forms.ModelForm):
    class Meta:
        model = TopScorer
        fields = ['title', 'info_1', 'info_2', 'info_3']
