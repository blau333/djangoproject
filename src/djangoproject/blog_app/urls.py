from django.urls import path
from djangoproject.blog_app import views

app_name = "blog"
urlpatterns = [
path("", views.index, name = "index"),
path("posts_list/", views.post_list, name = "post_list"),
path("post/<int:post_id>/", views.post_detail, name = "post_detail"),
path("post/<slug:post_slug>/", views.post_detail, name = "post_detail"),
path("categories/", views.categories_list, name = "categories_list"),
path("categories/<int:category_id>/", views.category_detail, name = "category_detail"),
path("create_post/", views.create_post, name="create_post")
]

