"""grumblr2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include, url


from django.conf import settings

from django.contrib import admin
from django.conf.urls.static import static

from django.urls import path,include

from django.conf.urls import include
from django.views.generic.base import TemplateView

from django.contrib.auth.views import (
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView,
)
urlpatterns = [

    url(r'^', include('grumblr_private.urls')), 

    # path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
    
    url(r'^user/', include('grumblr_private.urls')),

    path('grumblr-private/', include('grumblr_private.urls')),

    path('accounts/', include('accounts.urls')),

    path('accounts/', include('django.contrib.auth.urls')),

    path('password_reset/', PasswordResetView.as_view(template_name='password_reset.html'), name="password_reset"),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view( template_name ='password_reset_confirm.html'), name="password_reset_confirm"),
    path('reset/complete/', PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'), name="password_reset_complete"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)