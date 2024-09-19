import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    user_json = { "raw_document": { "text": text_to_analyse } }

    # Make the API request
    response = requests.post(url, headers=headers, json=user_json)
    
    # Check the status code and return the result
    if response.status_code == 200:
        return response.json()  # Return the JSON response
    else:
        return f"Error: {response.status_code} - {response.text}"

# could have code to call this