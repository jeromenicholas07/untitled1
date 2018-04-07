from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.urls import include

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),

    url(r'^tts', views.process_tts, name='tts'),
    url(r'^stt', views.stt, name='stt'),
    url(r'^sentiment-analysis', views.sentimentAnalysis, name='sentiment-analysis'),
    # url(r'^login', auth_views.login, name='login'),
    url(r'^accounts/signup', views.signup, name='signup'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]