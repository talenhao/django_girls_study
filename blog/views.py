from django.shortcuts import render

# Create your views here.
from .models import Post
from django.utils import timezone


def post_list(request):
    # QuerySet查询集
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {"posts": posts})
