from django.shortcuts import render
from django.http import HttpResponse
from .forms import EventForm
from .models import Event


def index(request): 
    if request.user.is_authenticated(): 
        Events=Event.objects.all()
    return render(request,'Events/index.html', {'Events' :Events})

def create_event(request): 
    form=EventForm(request.POST or None , request.FILES or None)
    if form.is_valid(): 
        Events=form.save(Commit=False)
        Events.save()
        return render(request, 'Events/details.html', {'event': Events})
    return render(request, 'Events/event_form.html', {'form': form})





def details(request, event_id): 
    Events=Event.objects.get(pk=event_id)
    return render(request, 'Events/details.html', {'event': Events})






def delete_event(request, event_id):
    Events=Event.objects.get(pk=event_id)
    Event.delete()
    return render(request, 'Events/index.html') 




def edit_event(request, event_id): 

    Events=Event.objects.get(pk=event_id)
    if request.method=="POST":  
       form=EventForm(request.POST ,instnace=Events)
       if form.is_valid(): 
        Events=form.save(Commit=False)
        Events.save()
        return render(request, 'Events/details.html', {'Events': Events})
    else: 
        form=EventForm(instnace=Events)
        return render(request, 'Events/event_form.html' ,{'form': form})

