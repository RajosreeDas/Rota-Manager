from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member
from django.contrib.auth.models import User

class UserBasicForm(UserCreationForm):
	email = forms.EmailField(label = "Email")

	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name']
class MemberForm(forms.ModelForm): 
    date_of_birth = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))

    date_of_joining = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))

    class Meta:
	    model = Member
	    fields = ['role', 'phone', 'address', 'date_of_birth', 'date_of_joining', 'blood_group', 'designation']






 