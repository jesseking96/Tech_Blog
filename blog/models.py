from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse_lazy

# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=500)
    text = models.CharField(max_length=2000)
    slug = models.SlugField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now=True)
    title_image = models.ImageField(upload_to='blog/post_title_images',default='blog/post_title_images/default.jpg')

    posted = False

    def publish(self):
        self.posted = True
        self.published_date = timezone.now()

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments',default=None)
    text = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse_lazy('single',slug=self.post.slug)
