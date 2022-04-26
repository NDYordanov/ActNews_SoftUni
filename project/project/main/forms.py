from django import forms

from project.common.helpers import BootstrapFormMixin
from project.main.models import Article


class CreateArticleForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Article
        # fields = ('title', 'category', 'image', 'summary')
        fields = '__all__'
        # widgets = {
        #     'title': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Enter article',
        #         }
        #     ),
        # }
