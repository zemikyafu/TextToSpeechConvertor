from flask import Flask, request, Response
from textToSpeechAzure import textToSpeechAzure
from textToSpeechAWS import textToSpeechAWS

# Initialize Flask app
app = Flask(__name__)
from flask_cors import CORS
CORS(app)



@app.route('/api/text-to-speech', methods=['POST'])
def text_to_speech():
    # Get text from POST request
    text = request.json['text']
    language = request.json['language']
    print(language)
    audio_data=textToSpeechAzure.textToSpeechWithAzure(text,language)
    if audio_data!=None:
        print("Conversion using Azure")
        return Response(audio_data, mimetype='audio/wav')
    else :
        audio_data=textToSpeechAWS.textToSpeechWithAWS(text,language)
        print("Conversion using AWS")
        return Response(audio_data, mimetype='audio/wav')
        

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5003)
