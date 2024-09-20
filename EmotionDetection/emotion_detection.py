import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    user_json = { "raw_document": { "text": text_to_analyze } }

    # Make the API request
    response = requests.post(url, headers=headers, json=user_json)
    
    # Check the status code and return the result
    if response.status_code == 200:
        formatted_emotion_response = format_emotion_response(response.json())
        return formatted_emotion_response # Return the JSON response
    
    # If not 200, we have an error.
    return f"Error: {response.status_code} - {response.text}"

def format_emotion_response(json):
    """
    This function formats the json to from the response and returns it as a dictionary.
    Specifically a dictionary with anger, disgust, fear, joy, sadness, and the name of the dominant emotion
    """
    EMOTION_KEY = "emotion"
    EMOTION_PREDICTIONS_KEY = "emotionPredictions"
    DOMINATE_EMOTION_KEY = "dominant_emotion"

    if not isinstance(json, dict) or EMOTION_PREDICTIONS_KEY not in json or EMOTION_KEY not in json[EMOTION_PREDICTIONS_KEY][0]:
        return None

    emotion_dict = json[EMOTION_PREDICTIONS_KEY][0][EMOTION_KEY]
    dominant_emotion = None
    dominant_emotion_score = 0

    # find the dominant emotion from the dict
    for emotion in emotion_dict:
        new_emotion_score = emotion_dict[emotion]
        
        if dominant_emotion_score < new_emotion_score:
            dominant_emotion_score = new_emotion_score
            dominant_emotion = emotion
    
    # add the dominant emotion to the dictionary
    emotion_dict[DOMINATE_EMOTION_KEY] = dominant_emotion
    return emotion_dict