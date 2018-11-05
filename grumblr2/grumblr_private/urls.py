
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import include
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [

    path('', views.index, name='index'),
    url(r'view$', views.get_user_profile, name = "view_profile"),
    url(r'edit$', views.edit_profile, name = "edit_profile"),
    url(r'following$', views.list_followers, name = "view_following"),
    url(r'^post/comment/(?P<pk>\d+)$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^/(?P<username>[a-zA-Z0-9]+)$', views.get_profile, name = "other"),
    url(r'change-password$', views.change_password, name = "change_password"),
    path(r'add-post', views.add_post),
    path(r'check-new-post', views.check_new_posts),

	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
	url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_followers, name='change_followers'),
		

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


