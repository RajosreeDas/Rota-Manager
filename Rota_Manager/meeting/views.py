from django.shortcuts import render

# Create your views here.
from .models import Meeting
from django.http import HttpResponse
from .forms import MeetingForm

def index(request): 
    if request.user.is_authenticated(): 
        meeting=Meeting.objects.all()
        return render(request, 'meeting/index.html' ,{'meeting': meeting})

def create_meeting(request): 
    form=MeetingForm(request.POST or None)
    if form.is_valid(): 
        meeting=form.save(Commit=False)
        Meeting.save()
        return render(request, 'meeting/details.html' ,{'meeting': meeting})
    return render(request, 'meeting/meeting_form.html', {'form': form})



def meeting_details(request, meeting_id): 
    meeting=Meeting.objects.get(pk=meeting_id)
    return render(request, 'meeting/details.form')




def edit_meeting(request, meeting_id): 
    meeting=Meeting.objects.get(pk=meeting_id)

    if request.method=="POST": 
        form=MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
           meeting=form.save(Commit=False)
           meeting.save()
        return render(request,'meeting/details.html',{'meeting': meeting})
    else: 
        form=MeetingForm(instance=meeting)
        return render(request,'meeting/meeting_form', {'form': form})



def delete_meeting(request, meeting_id): 
    meeting=Meeting.objects.get(pk=meeting_id)
    meeting.delete()
    return render(request, 'meeting/index.html')

