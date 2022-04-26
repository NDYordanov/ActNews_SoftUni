from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from project.common.view_mixins import RedirectToDashboard
from project.main.forms import CreateArticleForm
from project.main.models import Article


class HomePage(views.ListView):
    template_name = 'main/home_page.html'
    model = Article
    context_object_name = 'articles'


# class ArticleDetails(views.DetailView, id):
#     article = Article.objects.all().get(pk=id)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['article'] = self.article
#         return context


class CreateArticleView(RedirectToDashboard, views.CreateView):
    form_class = CreateArticleForm
    template_name = 'main/create_article.html'
    success_url = reverse_lazy('home page')
