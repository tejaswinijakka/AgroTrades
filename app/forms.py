from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
#from app.forms import Registration

class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    phno = forms.CharField(max_length=10)
    location = forms.CharField(max_length=50)
    usertype = forms.IntegerField()
    class Meta:
        model = User
        fields = ("username","first_name",'last_name','phno','location','usertype','password1','password2')
         
        

    '''def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["phno"].label = "Phone Number"
        self.fields["location"].label = "Location"
        self.fields["usertype"].label = "User Type"'''
