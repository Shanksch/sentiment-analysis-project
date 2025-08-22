from flask import Flask, request, jsonify
import joblib
import numpy as np
import re
from data_preprocessing import preprocess_text

try:
    model = joblib.load('lr_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    # Print a success message to the console to confirm that the models loaded correctly.
    print("Model and vectorizer loaded successfully.")
except FileNotFoundError:
    print("Error: Model or vectorizer file not found. Make sure 'lr_model.pkl' and 'tfidf_vectorizer.pkl' are in the same directory as app.py.")
    model = None
    vectorizer = None
except Exception as e:
    print(f"An error occurred while loading the model/vectorizer: {e}")
    model = None
    vectorizer = None

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'Invalid input: No JSON data received or content-type is not application/json.'}), 400
    except Exception as e:
        return jsonify({'error': f'An error occurred while parsing JSON: {str(e)}'}), 400

    # Check if the review text is valid
    review_text = data.get('review')
    if not review_text or not isinstance(review_text, str) or not review_text.strip():
        return jsonify({'error': 'The "review" field is missing, empty, or not a string.'}), 400
    
    cleaned_text = preprocess_text(review_text)
    try:
        text_vector = vectorizer.transform([cleaned_text])
    except Exception as e:
        return jsonify({'error': f'An error occurred during text vectorization: {str(e)}'}), 500
    
    try:
        prediction = model.predict(text_vector)
        sentiment = prediction[0]
    except Exception as e:
        return jsonify({'error': f'An error occurred during model prediction: {str(e)}'}), 500

    return jsonify({'sentiment': sentiment.title()}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=5000)
    