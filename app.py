from flask import Flask, request, jsonify
import joblib
import re
from data_preprocessing import preprocess_text

app = Flask(__name__)

# Lazy load models (load only once when first request comes in)
model = None
vectorizer = None

def load_model():
    global model, vectorizer
    if model is None or vectorizer is None:
        try:
            model = joblib.load('lr_model.pkl')
            vectorizer = joblib.load('tfidf_vectorizer.pkl')
            print("✅ Model and vectorizer loaded successfully.")
        except FileNotFoundError:
            print("❌ Error: Model or vectorizer file not found.")
        except Exception as e:
            print(f"❌ Error loading model/vectorizer: {e}")

@app.route("/")
def home():
    return jsonify({"message": "API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    load_model()  # ensure models are loaded
    if model is None or vectorizer is None:
        return jsonify({'error': 'Model not available'}), 500


    try:
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'Invalid input: No JSON data received or content-type is not application/json.'}), 400
    except Exception as e:
        return jsonify({'error': f'JSON parse error: {str(e)}'}), 400

    review_text = data.get('review')
    if not review_text or not isinstance(review_text, str) or not review_text.strip():
        return jsonify({'error': 'The "review" field is missing, empty, or not a string.'}), 400

    cleaned_text = preprocess_text(review_text)

    try:
        text_vector = vectorizer.transform([cleaned_text])
        prediction = model.predict(text_vector)
        sentiment = prediction[0]
    except Exception as e:
        return jsonify({'error': f'Prediction error: {str(e)}'}), 500

    return jsonify({'sentiment': sentiment.title()}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
