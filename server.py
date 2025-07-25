# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This function defines the function sent_detector
    '''

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the emotions and the dominant emotion from the response
    dominant_emotion = response['dominant_emotion']
    emotions = {key: response[key] for key in response if key != 'dominant_emotion'}

    # Check if the dominant emotion is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid input! Try again."

    # Format the response as specified
    emotion_details = ', '.join([f"'{emotion}': {score}" for emotion, score in emotions.items()])
    formatted_response = f"For the given statement, the system response is {emotion_details}. The dominant emotion is {dominant_emotion}."

    return formatted_response

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
    page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)