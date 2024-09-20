from EmotionDetection import emotion_detector
from flask import Flask, render_template, request

app = Flask("Emotion Detector")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotionDetector():
    # get the text from the request
    textToAnalyze = request.args.get('textToAnalyze')

    # get the emotion of the text
    result = emotion_detector(textToAnalyze)

    # successfully returned data, format it and render it to the template
    if result is not None:
        DOMINANT_EMOTION_KEY = "dominant_emotion"
        res_string = "For the given statement, the system response is "
        res_string += ", ".join(f"'{emotion}': {value:.9f}" for emotion, value in result.items() if emotion != DOMINANT_EMOTION_KEY)

        # Add the dominant emotion at the end
        res_string += f". The dominant emotion is <strong>{result[DOMINANT_EMOTION_KEY]}.</strong>"
        return res_string
    
    # else return error message
    return render_template('index.html', {"message": "The sentence you entered could not be analyzed! Try again."})

if __name__ == "__main__":
    app.run(debug=True)
    