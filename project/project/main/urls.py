from django.http import HttpResponse
from django.urls import path

from project.main.views import HomePage, CreateArticleView, ArticleDetails, EditArticleView, DeleteArticleView

urlpatterns = [
    path('', HomePage.as_view(), name='home page'),
    path('add_article/', CreateArticleView.as_view(), name='add article'),
    path('article/<int:pk>/', ArticleDetails.as_view(), name='details page'),
    path('article/edit/<int:pk>/', EditArticleView.as_view(), name='edit article page'),
    path('article/delete/<int:pk>', DeleteArticleView.as_view(), name='delete article page'),
]