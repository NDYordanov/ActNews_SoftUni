from django.http import HttpResponse
from django.urls import path

from project.main.views import HomePage




urlpatterns = [
    path('', HomePage.as_view(), name='home page'),
    # path('article/<ind:pk>', ArticleDetails.as_view(), name='details page'),
]