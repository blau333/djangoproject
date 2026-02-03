from django import forms
from djangoproject.blog_app.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "slug",
            "author",
            "content",
            "category",
            "published",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название статьи",
                }
            ),
            "slug": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите slug",
                }
            ),
            "author": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите текст статьи",
                    "rows": 5,
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

class CategoryForm(forms.Form):
    name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите название категории",
            }
        ),
    )