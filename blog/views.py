from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from watson_developer_cloud import TextToSpeechV1

from os.path import join, dirname
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
            text_to_speech = TextToSpeechV1(username='6424de64-aefa-417c-ae39-5ba79801f371', password='iCdJQmgYmOWD')

            with open(join(BASE_DIR, 'blog/static/output/out1.wav'), 'wb') as audio_file:
                audio_file.write(text_to_speech.synthesize('Hello world!', accept='audio/wav', voice="en-US_AllisonVoice").content)

            #ttsWatson = TtsWatson('6424de64-aefa-417c-ae39-5ba79801f371', 'iCdJQmgYmOWD', 'en-US_AllisonVoice')
            #ttsWatson.play(str(txt))
            return HttpResponseRedirect('/thanks/')
    else:
        form = ttsForm()
    return render(request, 'templates/tts.html', {'form': form})
