import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        score_list = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
        emotion_list = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']

        dominant_emotion_index = score_list.index(max(score_list))
        dominant_emotion = emotion_list[dominant_emotion_index]

    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score,
            'joy': joy_score, 'sadness': sadness_score, 
            'dominant_emotion': dominant_emotion}
