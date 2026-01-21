from django.http import HttpResponse
from djangoproject.blog_app.models import Post
from .models import Category
from django.shortcuts import render, get_object_or_404

def index(request):
    return HttpResponse("<h1>Привет, блог!</h1>")

def post_list(request):
    posts = Post.objects.filter(published=True)
    response_content = '<h1>Список статей</h1> <ul>'
    for post in posts:
        response_content += f'<li><a href="/post/{post.id}/">{post.title}</a> {post.created_at}</li>'
        response_content += "</ul>"
    return HttpResponse(response_content)
def post_detail(request, slug):
    post = get_object_or_404(Post, slug = slug, publshed=True)
    content = f'''
    <h1>{post.title}</h1>
    <p>Автор: {post.author.username}</p>
    <div>Контент:{post.content}</div>
    <hr>
    <a href="/posts_list/">Назад к статьям</a>
    '''
    return HttpResponse(content)

def categories_list(request):
    categories = Category.objects.all()
    return render(request, categories_list.html, {'categories': categories})

def category_detail(request, category_id):
    category = Category.objects.get_or_404(id=category_id)
    posts = Post.objects.filter(category=category, published=True)
    return render(request, category_detail.html, {'category': category, 'posts': posts})
