# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from post import views

urlpatterns =  [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list, name = 'post_list'),
    url(r'^(?P<sort_type>[\w-]+)/$', views.post_sort, name = 'post_sort'),
    url(r'^about/$', views.about, name = 'about'),
    url(r'^contacts/$', views.contacts, name = 'contacts'),
    url(r'^(?P<post_id>[0-9]+)/like/$', views.post_like, name = 'post_like'),
    url(r'^(?P<post_id>[0-9]+)/dislike/$', views.post_dislike, name = 'post_dislike'),
    url(r'^(?P<post_id>[0-9]+)/$', views.post_detail, name = 'post_detail'),
    url(r'^(?P<slug>[\w-]+)/$', views.post_by_category, name = 'post_by_category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
