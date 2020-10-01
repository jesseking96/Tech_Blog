from django.shortcuts import render
from django.views import generic
from .models import Post,Comment
from django.shortcuts import render,get_object_or_404
from .forms import CommentForm
# Create your views here.

class IndexView(generic.base.TemplateView):
    template_name = 'blog/index.html'

class PostListView(generic.list.ListView):
    model = Post

class PostDetailView(generic.detail.DetailView):
    model = Post

def new_comment(request,slug):
    template_name = 'blog/comment_form.html'
    post = get_object_or_404(Post,slug=slug)
    user = request.user
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post=post
            new_comment.user =user
            new_comment.save()
            return reverse_lazy('single',slug=post.slug)
    else:
        comment_form=CommentForm()

    return render(request,template_name,{'comment_form':comment_form})
