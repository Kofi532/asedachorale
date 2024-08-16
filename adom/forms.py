from django import forms

class HymnSearchForm(forms.Form):
    query = forms.CharField(label='Search Hymns', max_length=100)

# forms.py
from django import forms
from .models import AudioRecording

class AudioRecordingForm(forms.ModelForm):
    class Meta:
        model = AudioRecording
        fields = ['audio_data']
