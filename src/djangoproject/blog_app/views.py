from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from djangoproject.blog_app.forms import CategoryForm, PostForm
from djangoproject.blog_app.models import Post, Category
from django.shortcuts import render, redirect
from django.utils.text import slugify


def index(request):
    posts = Post.objects.filter(published=True).order_by("-created_at")[:5]

    context = {
        "posts":posts
    }
    return render(request, template_name="blog_app/index.html", context=context)

def post_list(request):
    posts = Post.objects.filter(published=True)
    response_content = '<h1>Список статей</h1> <ul>'
    for post in posts:
        response_content += f'<li><a href="/post/{post.id}/">{post.title}</a> {post.created_at}</li>'
        response_content += "</ul>"
    return HttpResponse(response_content)
def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    content = {
        "post": post
    }
    return render(request, template_name="blog_app/post_detail.html", context=content)

def categories_list(request):
    categories = Category.objects.all()
    response_content = '<h1>Список категорий</h1> <ul>'
    for category_a in categories:
        response_content += f'<li><a href="/category/{category_a.id}/">{category_a.title}</a></li>'
    response_content += '</ul>'
    return render(request, template_name="blog_app/categories_list.html", context=context)


def category_detail(request, category_id):
    category = get_object_or_404(Category, pk = category_id)
    posts = Post.objects.filter(topic=category)
    response_content = f"<h1> Категория: {category.title} </h1> <ul>"
    response_content += '<li><a href="/categories/">Перейти к категориям </a>'
    for post in posts:
        if post.published:
            post_published = "Опубликовано."
        else:
            post_published = "Не опубликовано."
        response_content += f'''
        <h2>{post.title}</h2>
        <p>автор: {post.author.username}</p>
        <div> контент:{post.content} </div>
        <div> публикация:{post_published} </div>
        <hr>
        <a href="/post/{post.slug}/">К статье>></a>
        '''
    return render(request, template_name="blog_app/category_detail.html", context=context)
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(new_post.title)
            new_post.save()

            return redirect("blog:post_detail", new_post.slug)
    else:
        form = PostForm()

    context = {
        "form": form
    }
    return render(request, "blog_app/create_post.html", context=context)

def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
           form.save()
           return redirect("blog:categories_list")
    else:
        form = CategoryForm()

    context = {
        "form": form
    }
    return render(request, "blog_app/create_category.html", context=context)

def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            edited_post = form.save(commit=False)
            edited_post.slug = slugify(edited_post.title)
            edited_post.save()

            return redirect("blog:post_detail", edited_post.slug)
    else:
        form = PostForm(instance=post)

    context = {
        "form": form,
        "post": post
    }
    return render(request, "blog_app/edit_post.html", context=context)
