from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('new/',views.SiteUserCreateView.as_view(),name='signup'),
    #path('new/profilecreate/',views.ProfileInfoCreateView.as_view(),name='profile_info_create'),
]
