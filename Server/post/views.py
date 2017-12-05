from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required

from .forms import CommentForm, PostForm
from .models import Post, Comment


@login_required
def post_list(request):
    post = Post.objects.filter(moder = True)
    return render(request, "post/post_list.html", {"posts": post})

def post_single(request, pk):
    post = get_object_or_404(Post, pk = pk)
    comment = Comment.objects.filter(post=post)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comm = form.save(commit = False)
            comm.user = request.user
            comm.post = post
            comm.save()
    else:
        form = CommentForm()
    return render(request, "post/post_single.html", {"post":post, "form": form,
                                                     "comment": comment})

def post_add(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.instance
            post.user = request.user
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()
    return render(request, "post/post_add.html", {"form": form})