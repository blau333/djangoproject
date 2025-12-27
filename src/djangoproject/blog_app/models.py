from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name='Категория'
        verbose_name_plural= 'Категории'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True)
    content = models.TextField(verbose_name='Содержание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name='Категория'
    )

    class Meta:
        verbose_name='Статья'
        verbose_name_plural= 'Статьи'
        ordering = ["created_at", "published"]

    published = models.BooleanField(default=False, verbose_name='Статус публикации')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Кол-во просмотров')

    def __str__(self):
        return self.title

    def increase_views_count(self):
        self.views_count += 1
        self.save(update_fields=["views_count"])
