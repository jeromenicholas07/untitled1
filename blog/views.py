from django.http import HttpResponseRedirect,HttpResponse
from django.utils import timezone
from watson_developer_cloud import TextToSpeechV1

import wave
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions, SentimentOptions, EmotionOptions

from os.path import join, dirname
import os
from django.forms import ValidationError
from .models import Post
from .forms import ttsForm, sentiForm


from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'templates/post_list.html', {'posts': posts})

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

def login(request):
    return render(request, 'templates/../registration/login.html')

# class signup(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def sentimentAnalysis(request):
    emotions = {'anger': 0, 'fear': 0, 'joy': 0, 'disgust': 0, 'sadness': 0}
    if request.method == 'POST' :
        form = sentiForm(request.POST)

        if form.is_valid():
            txt = form.cleaned_data['txt']

            if len(txt) < 24 :
                form.add_error('txt', 'More text required to process..')
                return render(request, 'templates/sentiment-analysis.html', {'form': form, 'emotions': emotions})
                # raise(ValidationError('More text required..', code='invalid'))

            natural_language_understanding = NaturalLanguageUnderstandingV1(
                username='3aceb54b-84ec-4f6a-ba0a-c61f0470c5b3',
                password='s7QSIEMHDxSp',
                version='2018-03-16')

            response = natural_language_understanding.analyze(
                text=txt,
                features=Features(emotion=EmotionOptions()))


            emotions =  response["emotion"]["document"]["emotion"]

            print(json.dumps(response, indent=2))
            return render(request, 'templates/sentiment-analysis.html', {'form': form, 'emotions': emotions})
    else :

        form = sentiForm()
        return render(request, 'templates/sentiment-analysis.html', {'form': form, 'emotions': emotions})


    #
    #
    # if request.method == 'POST':
    #     form = ttsForm(request.POST)
    #
    #     if form.is_valid():
    #         txt = form.cleaned_data['txt']
    #         text_to_speech = TextToSpeechV1(username='ab79ea31-5f07-4c63-94ec-82b526b9fcd8', password='ZCE3iPsVwLTc')
    #
    #         # op = text_to_speech.synthesize(text='Hello world!', accept='audio/wav', voice="en-US_AllisonVoice")
    #         path = 'blog/static/output/out1.wav'
    #         with open(path, 'wb+') as audio_file:
    #             audio_file.write(text_to_speech.synthesize(text=txt, accept='audio/wav', voice="en-US_AllisonVoice").content)
    #
    #             return render(request, 'templates/tts.html', {'form': form, 'audi': audio_file})
    #
    #         #ttsWatson = TtsWatson('6424de64-aefa-417c-ae39-5ba79801f371', 'iCdJQmgYmOWD', 'en-US_AllisonVoice')
    #         #ttsWatson.play(str(txt))
    #
    #
    #         with open(path, 'rb') as fsock:
    #             # Enabling this block will make the file available for download when submit is clicked
    #             response = HttpResponse(fsock.read(), {'form': form, 'audi': 'blog/static/output/out1.wav'})
    #             response['mime_type'] = 'audio/mpeg'
    #             response['Content-Disposition'] = 'attachment; filename="out1.wav"'
    #             return response
    # else:
    #     form = ttsForm()
    # return render(request, 'templates/tts.html', {'form': form, 'audi': ''})