from django import forms
from djangoproject.blog_app.models import Post
from djangoproject.blog_app.management.commands import utils

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", "slug", "author", "content", "published" ]
        widgets = {
              "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название статьи",
                }
            ),
            "author": "forms.select"(
                attrs={
                    "class": "form-select"
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control"
                    "placeholder": "Введите статью"
                }
            ),
            "Category": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
        }