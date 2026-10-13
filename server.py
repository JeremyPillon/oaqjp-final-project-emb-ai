"""
Flask server module for Emotion Detection API using Watson NLP runtime.
"""
from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """
    Renders the primary application HTML interface.
    """
    return render_template('index.html')


@app.route("/emotionDetector")
def sent_detector():
    """
    Analyzes input text and returns formatted emotion analysis output.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    