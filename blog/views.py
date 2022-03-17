from copyreg import clear_extension_cache
from pydoc import render_doc
from django.shortcuts import redirect, render
from .forms import PostForm
from .models import Post

def PostListView(request): 
    posts = Post.objects.all()
    title = "Blog - Home"
    template = 'blog/home.html'
    # data_2col = list(zip(data[::2], data[1::2]))
    context = {
        'title': title,
        'posts': posts,
        'posts_count': len(posts)
    }
    return render(request, template, context)

def about(request):
    return render(request, 'blog/about.html')

def PostCreateView(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            post = Post(
                author = cleaned_data['author'],
                title = cleaned_data['title'],
                content = cleaned_data['content'],
            )
            post.save()
            return redirect('blog-home')
        else:
            print("POST data is invalid")

    title = "Blog - Create"
    template = 'blog/post_create.html'
    context = {
        'title': title,
    }
    return render(request, template, context)

def PostUpdateView(request, pk):
    post = Post.objects.filter(id=pk)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            post.update(
                author = cleaned_data['author'],
                title = cleaned_data['title'],
                content = cleaned_data['content'],
            )
            return redirect('blog-detail', pk)
        else:
            print("POST data is invalid")

    title = "Blog - Update"
    template = 'blog/post_update.html'
    context = {
        'title': title,
        'post': post.first(),
    }
    return render(request, template, context)

def PostDetailView(request, pk):
    post = Post.objects.filter(id=pk)
    
    title = "Blog - Detail"
    template = 'blog/post_detail.html'
    context = {
        'title': title,
        'post': post.first(),
    }
    return render(request, template, context)

def PostDeleteView(request, pk):
    post = Post.objects.filter(id=pk)

    if request.method == "POST":
        post.delete()
        return redirect('blog-home')

    title = "Blog - Delete"
    template = 'blog/post_delete.html'
    context = {
        'title': title,
        'post': post.first(),
    }
    return render(request, template, context)





