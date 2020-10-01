from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('<slug:slug>/',views.PostDetailView.as_view(),name='single'),
    path('<slug:slug>/addcomment/',views.new_comment,name='new_comment'),

]
