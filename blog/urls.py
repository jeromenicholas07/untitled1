from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path,include

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),

    path('tts', views.process_tts, name='tts'),
    path('stt', views.stt, name='stt'),
    path('sentiment-analysis', views.sentimentAnalysis, name='sentiment-analysis'),
    # url(r'^login', auth_views.login, name='login'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]