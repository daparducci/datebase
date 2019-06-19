from django.forms import ModelForm
from .models import Match_notes

class NotesForm(ModelForm):
    class Meta:
        model = Match_notes
        fields = ['notes']