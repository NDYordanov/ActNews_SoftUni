from django import forms

from project.common.helpers import BootstrapFormMixin
from project.main.models import Article


class CreateArticleForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        pet = super().save(commit=False)

        pet.user = self.user
        if commit:
            pet.save()

        return pet

    class Meta:
        model = Article
        fields = ('title', 'category', 'image', 'summary')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter article',
                }
            ),
        }
