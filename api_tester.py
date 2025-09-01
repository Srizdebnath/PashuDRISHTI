import requests
import os


API_URL = "http://127.0.0.1:5000/predict"
IMAGE_PATH = "./testimage.jpeg"


if not os.path.exists(IMAGE_PATH):
    print(f"Error: The file '{IMAGE_PATH}' was not found.")
    print("Please update the IMAGE_PATH variable in this script.")
else:
    try:
        with open(IMAGE_PATH, 'rb') as image_file:
            
            
            files = {'file': (os.path.basename(IMAGE_PATH), image_file, 'image/jpeg')}
            
            print(f"[*] Sending request to {API_URL} with image: {os.path.basename(IMAGE_PATH)}")
            
            
            response = requests.post(API_URL, files=files)
            
            
            if response.status_code == 200:
                
                print("[+] Success! Server responded with:")
                print(response.json())
            else:
                    
                print(f"[-] Error: Server responded with status code {response.status_code}")
                print(f"[-] Response body: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"[-] An error occurred while making the request: {e}")