import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json=myobj, headers=header)
    
    # Parse the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # Access the first element in the emotionPredictions list
    emotions_data = formatted_response['emotionPredictions'][0]['emotion']
    
    # Extracting emotion scores
    anger = emotions_data['anger']
    disgust = emotions_data['disgust']
    fear = emotions_data['fear']
    joy = emotions_data['joy']
    sadness = emotions_data['sadness']
    
    # Create a dictionary of scores
    emotions = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    
    # Find the dominant emotion (highest score)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return the output format
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
