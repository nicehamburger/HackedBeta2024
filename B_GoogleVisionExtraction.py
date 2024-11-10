import os
from google.cloud import vision
from google.oauth2 import service_account

class GoogleVisionExtractor:
    def __init__(self, credentials_path):
        """Initialize the Google Vision client with service account credentials."""
        self.credentials_path = credentials_path
        self.client = self._initialize_client()

    def _initialize_client(self):
        """Initializes the Vision client using service account credentials."""
        credentials = service_account.Credentials.from_service_account_file(self.credentials_path)
        return vision.ImageAnnotatorClient(credentials=credentials)

    def extract_text_from_image(self, image_path, output_folder):
        """Extract text from image using Google Vision API."""
        # Load the image file
        with open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        # Perform text detection
        response = self.client.text_detection(image=image)

        # Extract detected text
        detected_texts = response.text_annotations

        # Check if any text was detected
        if not detected_texts:
            print(f"No text detected in image: {image_path}")
            return ""

        # Get the full text detected
        full_text = detected_texts[0].description
        print(f"Detected Text for {image_path}:\n")

        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Generate the output text file path with the same name as the image
        image_filename = os.path.basename(image_path)  # Get image file name (e.g., "1.jpg")
        text_filename = os.path.splitext(image_filename)[0] + '.txt'  # Replace extension with '.txt'
        output_file_path = os.path.join(output_folder, text_filename)

        # Save the extracted text to the output file
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(full_text)

        print(f"Text has been saved to {output_file_path}")

        return full_text