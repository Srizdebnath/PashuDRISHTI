PashuDRISHTI 🐾  
AI-Based Breed Identification for Indian Cattle & Buffaloes

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3-black.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.12-orange.svg)

PashuDRISHTI is a prototype created for the Smart India Hackathon 2025. This mobile-first web app leverages deep learning to recognize Indian cattle and buffalo breeds from images, addressing the challenge of breed misclassification in the national livestock database.

🎥 **Demo Video**  
[Watch the Demo (Google Drive)](https://drive.google.com/file/d/1sgwFi-tuUr90xRDLkqg-kD11bfz3YSbB/view?usp=sharing)

🚀 The Challenge  
The Bharat Pashudhan App (BPA), managed by the Government of India, is essential for livestock data management. However, Field Level Workers (FLWs) often misidentify animal breeds, resulting in inaccurate records. This affects genetic improvement, nutrition planning, and disease management across the dairy industry.

✨ Our Approach  
PashuDRISHTI offers a user-friendly, AI-driven support tool. FLWs can simply snap a photo of an animal, and the app instantly suggests the most likely breed along with a confidence score. This helps standardize breed identification and improves data quality for the BPA.

Key Features  
🧠 AI-Powered Recognition: Employs a fine-tuned MobileNetV2 Convolutional Neural Network for quick, precise predictions.  
📱 Mobile-Optimized Web App: Fully responsive and accessible from any smartphone browser—no installation needed.  
⚡ Instant Results: Delivers breed predictions and confidence scores within seconds.  
💡 Easy to Use: Designed for users with little to no technical background.

🛠️ Technology Stack & Architecture  
| Category   | Technology                                                      |
|------------|-----------------------------------------------------------------|
| Frontend   | HTML5, CSS3, Bootstrap 5, JavaScript (Fetch API)                |
| Backend    | Python 3, Flask (web server & API)                              |
| AI/ML      | TensorFlow, Keras (model training), NumPy, Pillow (image processing) |
| DevOps     | Google Colab (GPU training), Git & GitHub (version control)     |

**System Overview:**  
The app uses a straightforward client-server model:  
- **Client (Frontend):** Users access the web page, upload an image, and send it to the backend via POST.  
- **Server (Flask Backend):**  
  - Accepts the image file  
  - Preprocesses it (resizes to 224x224 pixels, normalizes)  
  - Passes it to the preloaded Keras model  
  - Gets prediction probabilities  
  - Returns a JSON response (e.g., `{"breed": "Gir", "confidence": 92.5}`)  
- **Client:** Receives the response and updates the UI with the predicted breed and confidence.

⚙️ Getting Started

To set up and run the project locally:

1. **Requirements:**  
   - Python 3.8 or higher  
   - Git

2. **Clone the Repository:**  
   ```bash
   git clone https://github.com/[Srizdebnath]/PashuDRISHTI.git
   cd PashuDRISHTI
   ```

3. **Set Up a Virtual Environment:**  
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Dependencies:**  
   A `requirements.txt` file is provided for convenience.  
   ```bash
   pip install -r requirements.txt
   ```
   *(To generate this file, run `pip freeze > requirements.txt` after installing the necessary libraries.)*

5. **Obtain the Trained Model:**  
   The trained AI model is not included in the repository. You’ll need to train it yourself (see below) and place the `breed_classifier.keras` file in the project’s root directory.

6. **Start the Application:**  
   ```bash
   python app.py
   ```
   The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

🤖 Model Training

The heart of this project is its AI model, built using transfer learning with MobileNetV2 for optimal accuracy and speed.

1. **Dataset:**  
   - Contains three breeds: Gir, Sahiwal, and Murrah, sourced from the web.  
   - Organized into training and validation folders as per Keras requirements.  
   - Download: [Open the Dataset (Google Drive Zip)](https://drive.google.com/file/d/15u084t5sDEH0QZ91m8_a3i3yrBRoW4mp/view?usp=sharing)

2. **Training Notebook:**  
   - The full training workflow is available in a Google Colab notebook, utilizing free GPU resources.  
   - [Open the Training Notebook](https://colab.research.google.com/drive/1lk9laiIJpq8X9KzZGrXbj9fnSt9iC_bH?usp=sharing)

3. **Training Steps:**  
   - Upload `dataset.zip` to your Google Drive  
   - Open the Colab notebook  
   - Mount your Drive and execute the cells sequentially. The notebook will:  
     - Unzip the dataset  
     - Set up data augmentation  
     - Build the model with custom classification layers on MobileNetV2  
     - Compile and train the model  
   - After training, download the resulting `breed_classifier.keras` file.

🛣️ Roadmap

This prototype demonstrates the concept effectively. Planned future enhancements include:

- **Dataset Expansion:** Incorporate more native Indian cattle and buffalo breeds.
- **Progressive Web App (PWA):** Transform into a PWA with TensorFlow.js for offline use.
- **Feedback Mechanism:** Allow FLWs to confirm predictions, enabling continuous model improvement.
- **API Integration:** Build a robust API for seamless connection with the Bharat Pashudhan App.