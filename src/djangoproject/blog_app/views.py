from multiprocessing import context
from django.http import HttpResponse
from djangoproject.blog_app.models import Post
from .models import Category 
from django.shortcuts import get_object_or_404
from django.shortcuts import render


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
    return render(request, template_name="blog_app/post_detail.html", context=context)

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
