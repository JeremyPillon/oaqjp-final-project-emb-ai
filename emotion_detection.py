import requests
import json

def emotion_detector(text_to_analyze):
    # Watson NLP Emotion Predict endpoint URL
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers required by Watson NLP
    headers = {"grpc-metadata-mm-model-id": "watson_ru_emotion_stock"}
    
    # Input JSON payload
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send POST request
    response = requests.post(url, json=myobj, headers=headers)
    
    # Parse JSON response
    formatted_response = response.json()
    
    # Extract required emotion scores
    if 'emotionPredictions' in formatted_response and len(formatted_response['emotionPredictions']) > 0:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotions.get('anger')
        disgust_score = emotions.get('disgust')
        fear_score = emotions.get('fear')
        joy_score = emotions.get('joy')
        sadness_score = emotions.get('sadness')
        dominant_emotion = max(emotions, key=emotions.get)
    else:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    # Return formatted dictionary output
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }