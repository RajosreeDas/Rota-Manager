from django import forms 
from .models import Event

class EventForm(forms.ModelForm):
    date= forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    
    class Meta:
        model = Event
        fields = ('name', 'avenue', 'chair', 'secretary', 'description')

    
