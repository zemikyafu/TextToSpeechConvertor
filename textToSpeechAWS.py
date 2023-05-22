import boto3
class textToSpeechAWS:
    def textToSpeechWithAWS (text,language):
        
            aws_access_key_id = ''
            aws_secret_access_key = ''
            region_name = 'us-east-1'  
            polly = boto3.client('polly', region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
            voiceId =textToSpeechAWS.get_voice_id(language)
            print(voiceId)
            response = polly.synthesize_speech(
                Text=text,
                # OutputFormat='pcm',
                OutputFormat='mp3',
                VoiceId= voiceId,
                Engine='neural' 
            )
            
            # get audio response form AWS polly service 
            audio_stream = response['AudioStream'].read()
            # Save the audio stream to a file
            output_file = 'output.mp3'
            with open(output_file, 'wb') as file:
                file.write(audio_stream)
            with open(output_file, 'rb') as f:
                         audio_data = f.read()

            return audio_data
    
    # dictionary wirh corresponding Polly voiceId values
    def get_voice_id(language):
        voice_ids = {
            'ar': 'Hala',
            'en': 'Joanna',
            'fi': 'Suvi',
            'de': 'Vicki',
            'du': 'Laura'
        }
        
        return voice_ids.get(language)
