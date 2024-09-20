"""Flask application for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main index page."""
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detector_route():
    """Analyze the text and return the detected emotions."""
    dominant_emotion_key = "dominant_emotion"
    error_text = "<strong>Invalid text! Please try again!</strong>"

    # Get the text from the request
    text_to_analyze = request.args.get('textToAnalyze')

    # Ensure valid text is provided
    if not text_to_analyze:
        return error_text

    # Get the emotion analysis result
    result = emotion_detector(text_to_analyze)

    # If the result is None or doesn't contain the expected key, return an error
    if not result or dominant_emotion_key not in result:
        return error_text

    # Build the response string, excluding the dominant emotion key in the emotions
    res_string = "For the given statement, the system response is "
    res_string += ", ".join(
        f"'{emotion}': {value:.9f}"
        for emotion, value in result.items()
        if emotion != dominant_emotion_key
    )
    # Add the dominant emotion at the end
    res_string += f". The dominant emotion is <strong>{result[dominant_emotion_key]}.</strong>"

    return res_string


if __name__ == "__main__":
    app.run(debug=True)
