from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.
class SiteUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=get_user_model())
    profile_pic = models.ImageField(upload_to='accounts/user_profile_pics',default='blog/post_title_images/default.jpg',null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
