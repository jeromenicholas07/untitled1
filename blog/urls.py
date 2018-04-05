from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path,include

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^tts', views.process_tts, name='tts'),
    url(r'^stt.html', views.stt, name='stt'),
    # url(r'^login', auth_views.login, name='login'),
    # url(r'^signup', auth_views.auth_logout, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]