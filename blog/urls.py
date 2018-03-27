from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^tts.html', views.process_tts, name='tts'),
    url(r'^stt.html', views.stt, name='stt'),

]