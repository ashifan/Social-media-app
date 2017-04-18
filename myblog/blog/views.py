from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from blog.models import Post
from django.urls import reverse
from blog.forms import PostForm
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).\
                                order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect(reverse('blog:post_detail',
                            kwargs={'pk': post.pk}))
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect(reverse('blog:post_detail', kwargs={pk:post.pk}))
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})




def like_category(request):

    post_id = None
    if request.method == 'GET':
        post_id = request.GET['like_id']

    likes = 0
    if post_id:
        post = Post.objects.get(id=int(post_id))
        if post:
            likes = post.likes + 1
            post.likes =  likes
            post.save()

    return HttpResponse(likes)


def unlike_category(request):

    post_id = None
    if request.method == 'GET':
        post_id = request.GET['dislike_id']

    unlikes = 0
    if post_id:
        post = Post.objects.get(id=int(post_id))
        if post:
            unlikes = post.dislikes + 1
            post.dislikes =  unlikes
            post.save()

    return HttpResponse(unlikes)
