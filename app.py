import os
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from PIL import Image
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model_path = 'breed_classifier.keras'
model = tf.keras.models.load_model(model_path)
# Define the class names
class_names = ['gir', 'murrah', 'sahiwal'] 

# Function to preprocess the image
def preprocess_image(image):
    img = image.resize((224, 224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0) # Create a batch
    img_array = img_array / 255.0 # Rescale
    return img_array

# Define the home page route
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Define the predict route
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        try:
            # Open the image file
            image = Image.open(file.stream).convert('RGB')

            # Preprocess the image
            processed_image = preprocess_image(image)

            # Make prediction
            prediction = model.predict(processed_image)
            
            # Get the class with the highest probability
            predicted_class_index = np.argmax(prediction[0])
            predicted_class_name = class_names[predicted_class_index]
            confidence = float(prediction[0][predicted_class_index])

            return jsonify({
                'breed': predicted_class_name.capitalize(),
                'confidence': round(confidence * 100, 2)
            })
        except Exception as e:
            return jsonify({'error': str(e)})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)