
from django.urls import path
from djangoproject.blog_app import views
app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.post_list, name="post_list"),
    path("post/<slug:post_slug>/", views.post_detail, name="post_detail"),
    path("categories/", views.categories_list, name="categories_list"),
    path("category/<int:category_id>/", views.category_detail, name="category_detail"),
    path("post/create/", views.post_create, name="post_create"),
    path("category/create/", views.category_create, name="category_create"),
    path("post/<int:post_id>/edit/", views.post_edit, name="post_edit")
]
