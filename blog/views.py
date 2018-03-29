from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from django.utils import timezone
from watson_developer_cloud import TextToSpeechV1
import wave
import json

from os.path import join, dirname
import os
from .models import Post
from .forms import ttsForm
from untitled1.settings import BASE_DIR

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'templates/post_list.html', {'posts': posts})

def tts(request):
    return render(request, 'templates/tts.html')

def stt(request):
    return render(request, 'templates/stt.html')

def process_tts(request):
    if request.method == 'POST':
        form = ttsForm(request.POST)

        if form.is_valid():
            txt = form.cleaned_data['txt']
            text_to_speech = TextToSpeechV1(username='ab79ea31-5f07-4c63-94ec-82b526b9fcd8', password='ZCE3iPsVwLTc')

            # op = text_to_speech.synthesize(text='Hello world!', accept='audio/wav', voice="en-US_AllisonVoice")
            path = 'blog/static/output/out1.wav'
            with open(path, 'wb+') as audio_file:
                audio_file.write(text_to_speech.synthesize(text=txt, accept='audio/wav', voice="en-US_AllisonVoice").content)

                return render(request, 'templates/tts.html', {'form': form, 'audi': audio_file})

            #ttsWatson = TtsWatson('6424de64-aefa-417c-ae39-5ba79801f371', 'iCdJQmgYmOWD', 'en-US_AllisonVoice')
            #ttsWatson.play(str(txt))


            with open(path, 'rb') as fsock:
                # Enabling this block will make the file available for download when submit is clicked
                response = HttpResponse(fsock.read(), {'form': form, 'audi': 'blog/static/output/out1.wav'})
                response['mime_type'] = 'audio/mpeg'
                response['Content-Disposition'] = 'attachment; filename="out1.wav"'
                return response
    else:
        form = ttsForm()
    return render(request, 'templates/tts.html', {'form': form, 'audi': ''})
