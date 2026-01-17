from django.http import HttpResponse
from djangoproject.blog_app.models import Post

def index(request):
    return HttpResponse("<h1>Привет, блог!</h1>")

def post_list(request):
    posts = Post.objects.filter(published=True)
    response_content = '<h1>Список статей</h1> <ul>'
    for post in posts:
        response_content += f'<li><a href="/post/{post.id}/">{post.title}</a> {post.created_at}</li>'
        response_content += "</ul>"
    return HttpResponse(response_content)
def post_detail(request, post_id):
    post = Post.objects.get(pk = post_id)
    content = f'''
    <h1>{post.title}</h1>
    <p>Автор: {post.author.username}</p>
    <div>Контент:{post.content}</div>
    <hr>
    <a href="/posts_list/">Назад к статьям</a>
    '''
    return HttpResponse(content)
