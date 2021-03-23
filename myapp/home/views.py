from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from post.forms import PostForm
from post.models import Post, Like


@login_required
def home(request):
    initial_dict = {'user': request.user}
    form = PostForm(request.POST or None, initial=initial_dict)
    context = {
        "user": request.user,
        "form": form,
        "posts": Post.objects.all(),
        "my_likes_ids":Like.objects.filter(
            user=request.user).values_list('post_id', flat=True),
    }
    return render(request, 'home.html', context)

