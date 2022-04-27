from django import forms
from django.contrib.auth import get_user_model

from project.common.helpers import BootstrapFormMixin
from project.main.models import Article

UserModel = get_user_model()


class CreateArticleForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'image', 'summary']