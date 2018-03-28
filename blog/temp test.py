from django.http import HttpResponse
from watson_developer_cloud import TextToSpeechV1
import wave
from untitled1.settings import BASE_DIR

from os.path import join
txt = 'hello world!'
text_to_speech = TextToSpeechV1(username='ab79ea31-5f07-4c63-94ec-82b526b9fcd8', password='ZCE3iPsVwLTc')

op = text_to_speech.synthesize(text='Hello world!', accept='audio/wav', voice="en-US_AllisonVoice")

print(type(op))

response = HttpResponse(content_type='audio/wav')
response['Content-Disposition'] = 'attachment; filename="out1.wav"'

print(response)
with open('../blog/static/output/out1.wav', 'wb') as audio_file:
    audio_file.write(text_to_speech.synthesize(text='Hello world!', accept='audio/wav', voice="en-US_AllisonVoice").content)