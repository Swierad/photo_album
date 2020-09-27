"""photoalbum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from photo_album import views as pa_views

urlpatterns = [
    path('', pa_views.PhotoAlbumView.as_view(), name="index"),
    path('login', pa_views.UserLoginView.as_view(), name="user-login"),
    path('create', pa_views.UserCreateView.as_view(), name="user-create"),
    path('photo/<int:pk>', pa_views.CommentCreateView.as_view(), name="add-comment"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
