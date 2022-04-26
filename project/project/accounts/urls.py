from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from project.accounts.views import UserLoginView, UserRegisterView, UserDetailsView, ChangeUserPasswordView, LogOutView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', LogOutView.as_view(), name='logout user'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('<int:pk>/', UserDetailsView.as_view(), name='profile details'),
    path('change-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('home page')), name='password_change_done'),
]