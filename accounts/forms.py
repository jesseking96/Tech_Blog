from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class SiteUserCreateForm(UserCreationForm):
    class Meta():
        model = get_user_model()
        fields = 'username','password1','password2'

class ProfileInfoCreateForm(forms.ModelForm):

    class Meta():
      model = models.SiteUser
      fields = ('profile_pic',)
