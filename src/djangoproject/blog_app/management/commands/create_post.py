from django.core.management.base import BaseCommand
from djangoproject.blog_app.models import Post


class Command(BaseCommand):
    help = 'Создание поста в интерактивном режиме'

    def handle(self, *args, **options):
        title = input("Введите заголовок: ").strip()
        content = input("Введите текст поста: ").strip()

        if not title or not content:
            self.stdout.write(
                self.style.ERROR("Заголовок и текст не могут быть пустыми")
            )
            return

        if Post.objects.filter(title=title).exists():
            self.stdout.write(
                self.style.WARNING("Пост с таким заголовком уже существует")
            )
            return

        post = Post.objects.create(title=title, content=content)

        self.stdout.write(
            self.style.SUCCESS(f"Пост успешно создан → ID {post.id}")
        )
