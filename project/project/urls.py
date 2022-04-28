from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.main.urls')),
    path('accounts/', include('project.accounts.urls')),
    path('weather/', include('project.weather.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
