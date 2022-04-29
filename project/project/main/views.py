from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse_lazy
from django.views import generic as views
from project.common.view_mixins import RedirectToDashboard
from project.main.forms import CreateArticleForm, EditArticleForm, DeleteArticleForm
from project.main.models import Article


class HomePage(views.ListView):
    template_name = 'main/home_page.html'
    model = Article
    context_object_name = 'articles'


class ArticleDetails(views.DetailView):
    model = Article
    template_name = 'main/article_details.html'
    context_object_name = 'article'


class CreateArticleView(views.CreateView):
    form_class = CreateArticleForm
    template_name = 'main/create_article.html'
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        article = form.save(commit=False)
        article.journalist = self.request.user
        article.save()
        return super().form_valid(form)


class EditArticleView(views.UpdateView):
    template_name = 'main/edit-article.html'
    model = Article
    fields = '__all__'
    success_url = reverse_lazy('home page')


class DeleteArticleView(views.DeleteView):
    model = Article
    fields = '__all__'
    template_name = 'main/delete_article.html'
    success_url = reverse_lazy('home page')


def handler404(request):
    response = render('404.html', {}, context=RequestContext(request))
    response.status_code = 404
    return response
