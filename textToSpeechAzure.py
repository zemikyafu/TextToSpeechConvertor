import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import ResultReason
from flask import Response
import json
class textToSpeechAzure:
    def textToSpeechWithAzure (text,language):
            # Azure  text to speach Services access codes
            region = 'eastus2'
            subscription_key = ''
            endpoint= ''

            #  speech configuration 
            speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
            
             # set the voice ID
            speech_config.speech_synthesis_voice_name = textToSpeechAzure.get_voice_id(language)
        
            #  WAV form output
            audio_config = speechsdk.audio.AudioOutputConfig(filename='audio.wav')
            
            
            synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
            
               
            successfull=True
            audio_data=None
       
            try:
            # Synthesize text to speech
                 result = synthesizer.speak_text_async(text).get()
                 if result.reason == ResultReason.SynthesizingAudioCompleted:
                      print("Azure text to speech convertion complited")
                      with open('audio.wav', 'rb') as f:
                         audio_data = f.read()
                      return audio_data
                 else:
                      print("Azure text to speech convertion failed")
                      return None
                      
            except Exception as ex:
                 print("error: {}".format(ex))
                 return None
            
            # # dictionary wirh corresponding Azure voiceId values
            
    def get_voice_id(language):
               voice_ids = {
                    'ar': 'ar-EG-OmarNeural',
                    'am': 'am-ET-TirhasNeural',
                    'fi': 'fi-FI-SelmaNeural',
                    'de': 'de-DE-KatjaNeural',
                    'en': 'en-US-AriaNeural',
                    'du': 'nl-NL-ColetteNeural'
               
               }

               return voice_ids.get(language)     
  