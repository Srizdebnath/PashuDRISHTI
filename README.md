# PashuDRISHTI 🐾
### AI-Based Breed Identification for Indian Cattle & Buffaloes

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3-black.svg)](https://flask.palletsprojects.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.12-orange.svg)](https://www.tensorflow.org/)

PashuDRISHTI is a prototype created for the Smart India Hackathon 2025. This mobile-first web app leverages deep learning to recognize Indian cattle and buffalo breeds from images, addressing the challenge of breed misclassification in the national livestock database.

🎥 **Demo Video**  
[Watch the Demo (Google Drive)](https://drive.google.com/file/d/1sgwFi-tuUr90xRDLkqg-kD11bfz3YSbB/view?usp=drive_link)

---

### 🚀 The Challenge
The Bharat Pashudhan App (BPA), managed by the Government of India, is essential for livestock data management. However, Field Level Workers (FLWs) often misidentify animal breeds, resulting in inaccurate records. This affects genetic improvement, nutrition planning, and disease management across the dairy industry.

### ✨ Our Approach
PashuDRISHTI offers a user-friendly, AI-driven support tool. FLWs can simply snap a photo of an animal, and the app instantly suggests the most likely breed along with a confidence score. This helps standardize breed identification and improves data quality for the BPA.

#### Key Features
*   **🧠 AI-Powered Recognition:** Employs a fine-tuned MobileNetV2 Convolutional Neural Network for quick, precise predictions.
*   **📱 Mobile-Optimized Web App:** Fully responsive and accessible from any smartphone browser—no installation needed.
*   **⚡ Standalone API Service:** The backend functions as a robust API, ready for seamless integration with other applications like the official BPA.
*   **💡 Easy to Use:** Designed for users with little to no technical background.

### 🛠️ Technology Stack & Architecture
| Category   | Technology                                                      |
|------------|-----------------------------------------------------------------|
| Frontend   | HTML5, CSS3, Bootstrap 5, JavaScript (Fetch API)                |
| Backend    | Python 3, Flask (web server & API)                              |
| AI/ML      | TensorFlow, Keras (model training), NumPy, Pillow (image processing) |
| DevOps     | Google Colab (GPU training), Git & GitHub (version control)     |

**System Overview:**  
The app uses a client-server model where the backend exposes a prediction API:
- **Client (Web Frontend):** Users access the web page, upload an image, and send it to the backend via a POST request.
- **Server (Flask Backend):**
  - Exposes a `/predict` endpoint that accepts image files.
  - Preprocesses the image (resizes to 224x224 pixels, normalizes).
  - Passes it to the preloaded Keras model for inference.
  - Returns a JSON response (e.g., `{"breed": "Gir", "confidence": 92.5}`).
- Any client, including our web UI or another application, can consume this API.

### ⚙️ Getting Started

To set up and run the project locally:

1.  **Prerequisites:**
    *   Python 3.8 or higher
    *   Git

2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Srizdebnath/PashuDRISHTI.git
    cd PashuDRISHTI
    ```

3.  **Set Up a Virtual Environment:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Install Dependencies:**
    A `requirements.txt` file is provided for convenience.
    ```bash
    pip install -r requirements.txt
    ```

5.  **Obtain the Trained Model:**
    The AI model is not in the repository due to its size. You’ll need to train it yourself (see "Model Training" section) and place the `breed_classifier.keras` file in the project’s root directory.

6.  **Start the Application:**
    ```bash
    python app.py
    ```
    The web server will start and be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

### 🚀 API Usage & Testing

The core of our solution is a standalone API. You can test the prediction endpoint directly using the provided `api_tester.py` script.

1.  **Start the Server:** Make sure the Flask application is running in one terminal.
    ```bash
    python app.py
    ```

2.  **Prepare the Tester Script:**
    *   Open the `api_tester.py` file.
    *   Modify the `IMAGE_PATH` variable to point to a valid test image on your computer.

3.  **Run the Tester:**
    *   Open a **second terminal** and activate the same virtual environment.
    *   Run the script:
    ```bash
    python api_tester.py
    ```

4.  **Expected Output:**
    The script will call the API and print the JSON response directly to your terminal.
    ```json
    [*] Sending request to http://127.0.0.1:5000/predict with image: your_test_image.jpg
    [+] Success! Server responded with:
    {'breed': 'Gir', 'confidence': 94.12}
    ```

---

### 🤖 Model Training

The AI model was built using transfer learning with MobileNetV2 for optimal accuracy and speed.

1.  **Dataset:**
    *   Contains three breeds: Gir, Sahiwal, and Murrah, sourced from the web.
    *   Organized into training and validation folders as per Keras requirements.
    *   **Download:** [PashuDRISHTI Dataset (Google Drive ZIP)](https://drive.google.com/file/d/15u084t5sDEH0QZ91m8_a3i3yrBRoW4mp/view?usp=sharing)

2.  **Training Notebook:**
    *   The full training workflow is available in a Google Colab notebook, utilizing free GPU resources.
    *   **Open:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1lk9laiIJpq8X9KzZGrXbj9fnSt9iC_bH?usp=sharing)

3.  **Training Steps:**
    *   Upload `dataset.zip` to your Google Drive.
    *   Open the Colab notebook, mount your Drive, and execute the cells sequentially.
    *   The notebook will unzip the data, set up augmentation, build, compile, and train the model.
    *   After training, download the resulting `breed_classifier.keras` file.

---

### 🛣️ Roadmap

This prototype demonstrates the concept effectively. Planned future enhancements include:

-   **Dataset Expansion:** Incorporate more native Indian cattle and buffalo breeds.
-   **Progressive Web App (PWA):** Transform into a PWA with TensorFlow.js for offline use.
-   **Feedback Mechanism:** Allow FLWs to confirm predictions, enabling continuous model improvement.
-   **API Integration:** Build a robust and secure API for seamless connection with the official Bharat Pashudhan App.