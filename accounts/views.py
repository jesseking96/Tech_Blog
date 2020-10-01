from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.
from . import models, forms
class SiteUserCreateView(CreateView):
    form_class=forms.SiteUserCreateForm
    success_url = reverse_lazy('index')
    template_name = 'accounts/signup.html'

# class ProfileInfoCreateView(CreateView):
#    form_class = forms.ProfileInfoCreateForm
#    success_url='blog/index'
#    template_name = 'accounts/profile_create.html'
