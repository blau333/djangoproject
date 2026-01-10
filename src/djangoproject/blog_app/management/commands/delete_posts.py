from django.core.management.base import BaseCommand
from djangoproject.blog_app.models import Post


class Command(BaseCommand):
    help = 'Удаляет пост по заголовку'

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Заголовок поста')

    def handle(self, *args, **options):
        title = options['title']

        posts = Post.objects.filter(title=title)

        if not posts.exists():
            self.stdout.write(
                self.style.ERROR("Пост с таким заголовком не найден")
            )
            return

        if posts.count() > 1:
            self.stdout.write(
                self.style.WARNING("Найдено несколько постов, удаление отменено")
            )
            return

        confirm = input("Вы уверены, что хотите удалить пост? (yes/no): ")

        if confirm.lower() != 'yes':
            self.stdout.write("Удаление отменено")
            return

        posts.first().delete()
        self.stdout.write(
            self.style.SUCCESS("Пост успешно удалён")
        )
