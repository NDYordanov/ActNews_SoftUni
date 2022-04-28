from django import forms
from django.contrib.auth import get_user_model

from project.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from project.main.models import Article

UserModel = get_user_model()


class CreateArticleForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'image', 'summary']


class EditArticleForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class DeleteArticleForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Article
        fields = '__all__'
