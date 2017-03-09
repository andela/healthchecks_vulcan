from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from hc.blog.forms import PostForm
from hc.blog.models import Post, Category
from django.contrib.auth.decorators import login_required


def post_list(request):
    # Retrieve all posts from database and save to dictionary
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    all_posts = []
    for article in posts:
        one_article = {
            "title":article.title,
            "text":article.text[:100]+"...",
            "published_date":article.published_date,
            "pk":article.pk
        }
        all_posts.append(one_article)
    return render(request, 'blog/post_list.html', {'posts': all_posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
