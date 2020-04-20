from django.shortcuts import render

# Create your views here.
from .models import Member
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import MemberForm, UserBasicForm
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from django.contrib.auth.models import User

from django.views import generic

def index(request): 
    user=User.objects.all()
    if request.user.is_authenticated(): 
      return render(request, 'Account/index.html' ,{'user': user})
    else: 
      return render(request, 'Account/login.html')



def user_register(request): 
    form=UserBasicForm(request.POST or None) 
    member_form= MemberForm(request.POST or None)

    if form.is_valid() and member_form.is_valid():
        user = form.save(commit=False)
        member = member_form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']   #password1 and password2(confirm_password) are the two variables in UserCreationForm 
        email = form.cleaned_data['email']
        user.set_password(password)
        user.save()
       
        user = authenticate(username=username, password=password)
        if user is not None: 
            if user.is_active(): 
                member.user=user
                role=member_form.cleaned_data['role']
                if role=='ADMIN': 
                  user.is_superuser=True
                member.save()
                request(login, user)
                return render(request, 'dashboard/index.html', {'user': user})
        else:
            return render(request, 'Account/register.html', {'error': 'The user is no onger active'})
    return render(request, 'accounts/register.html',  {'form': form, 'member_form': member_form})


def user_login(request):
    if not request.user.is_authenticated: 
        if request.user=="POST": 
            username = request.POST['username']
            password = request.POST['password']
            user=authenticate(username=username, password=password)
            #ifuserisnotbanned
            if user is not None: 
                if user.is_active(): 
                    login(request, user)
                    return render(request, 'dashboard/index.html', {'success':'Successful'})
                else:
                 return render(request, 'Account/register.html', {'error':'Your account is no longer active'})
            return render(request, 'Account/login.html', {'error':'Credentials not found'})
        return render(request, 'Account/register.html')
    return render(request, 'accounts/dashboard.html' )


def edit_user(request, user_id): 
    user=User.objects.get(pk=user_id)
    if request.user=="POST": 
        form=UserBasicForm(request.POST, instance=user)
        member_form=MemberForm(request.POST , instance=user.member)
        if form.is_valid() and member_form.is_valid(): 
            user=form.save(commit=False)
            member=form.save(commit=False)
            username=form.cleaned_data['Username']
            password=form.cleaned_data['Password']
            email=form.cleaned_data['email']
            user.set_password(password)
            user.save()

            role=member_form.cleaned_data['role']
            if role =='ADMIN': 
                user.is_superuser= True
                user.is_staff = True
            else: 
                user.is_superuser= False
                user.is_staff = False
            member.save()
            user.save()

            user=User.objects.all()
            return render(request, 'Account/index.html', {'user': user})
        return render(request, 'Account/register.html', {'form': form, 'member_form': member_form})

    else: 
        form=UserBasicForm(instance=user)
        member_form=MemberForm(instance=user.member)
    return render(request, 'Account/register.html', {'form': form , 'member_form': member_form})


def delete_user(request, user_id): 
    user=User.objects.get(pk=user_id)
    user.delete()
    user=User.objects.all()
    return render(request, 'Account/index.html', {'user': user})


def user_logout(request): 
    logout(request)
    return request(request, 'Account/login.html')


def profile(request, user_id): 
    if request.user.is_authenticated:
        if user_id: 
            return render (request, 'Account/profile.html', {'user': User.objects.get(pk=user_id), 'user_now': request.user})
        else: 
            return render(request, 'Account/profile.html', {'user':User.request})
    return render(request, 'Account/login.html')
