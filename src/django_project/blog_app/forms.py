from django import forms
from blog_app.models import Post, Category
from blog_app.management.commands import utils


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "category", "published", "image"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название статьи",
                }
            ),
            "category": forms.Select(attrs={"class": "form-select"}),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите содержание статьи",
                    "rows": 10,
                }
            ),
            "published": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        subject = cleaned_data.get("title")
        category_available = (
            Category.objects.filter(title=subject).exclude(pk=self.instance.pk).exists()
        )
        if category_available:
            self.add_error("title", "Категория с данным названием уже существует")
        return cleaned_data


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название категории",
                }
            )
        }

    def clean(self):
        cleaned_data = super().clean()
        subject = cleaned_data.get("title")
        category_available = (
            Category.objects.filter(title=subject).exclude(pk=self.instance.pk).exists()
        )
        if category_available:
            self.add_error("title", "Категория с данным названием уже существует")
        return cleaned_data
