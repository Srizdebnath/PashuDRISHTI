import os
from flask import Flask
app = Flask(__name__)
# Load the model
model = None
try:
    model = tf.keras.models.load_model('model.h5')
except Exception as e:
    print(f'Error loading model: {e}')
    model = None

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return 'Model not loaded'
    # Use the loaded model for prediction
    return 'Prediction result'
