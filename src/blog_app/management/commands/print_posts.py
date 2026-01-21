from django.core.management.base import BaseCommand
from djangoproject.blog_app.models import Post


class Command(BaseCommand):
    help = 'Печатает все доступные посты'

    def handle(self, *args, **options):
        posts_count = Post.objects.count()

        if posts_count == 0:
            self.stdout.write(self.style.ERROR("Нет ни одного поста"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Найдено постов: {posts_count}\n"))

            for index, post in enumerate(Post.objects.order_by('created_at'), start=1):
                self.stdout.write(
                    f"{index}. "
                    f"Заголовок: {post.title} | "
                    f"Дата: {post.created_at.strftime('%d.%m.%Y')}"
                )
