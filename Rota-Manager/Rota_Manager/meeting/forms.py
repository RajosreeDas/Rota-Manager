from django import forms
from .models import Meeting

class MeetingForm(forms.ModelForm): 
    date= forms.DateField()
    time= forms.TimeField()

class Meta: 
    model= Meeting
    fields= ['number', 'agenda', 'venue', 'minutes', 'resolution']
    

