from django.http import HttpResponse
from django.urls import path

from project.main.views import HomePage, CreateArticleView, ArticleDetails

urlpatterns = [
    path('', HomePage.as_view(), name='home page'),
    path('add_article/', CreateArticleView.as_view(), name='add article'),
    path('article/<int:pk>/', ArticleDetails.as_view(), name='details page'),
]