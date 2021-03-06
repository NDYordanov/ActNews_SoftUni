from django.contrib.auth import views as auth_views, get_user_model
from django.views import generic as views
from django.urls import reverse_lazy
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy

from project.accounts.forms import CreateProfileForm
from project.accounts.models import Profile
from project.common.view_mixins import RedirectToDashboard
from project.main.models import Article

ModelUser = get_user_model()


class UserRegisterView(RedirectToDashboard, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/register_page.html'
    success_url = reverse_lazy('home page')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('home page')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object is a Profile instance
        articles = list(Article.objects.filter(journalist_id=self.object.user_id))

        context.update({
            'total_articles': len(articles),
            'articles': articles,
        })

        return context


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    template_name = 'accounts/change_password.html'


class LogOutView(auth_views.LogoutView):
    template_name = 'main/home_page.html'
