from django.urls import path
from . import views
from .views import categories_list

app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),
    path('posts_list/', views.post_list, name='posts_list'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('categories/', categories_list, name='categories_list'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail')
    ]
