import json
import requests
import os
from post import *
from postcollections import *
from event import *
from eventcollections import *
from B_GoogleVisionExtraction import *

# Main Script: GoogleVisionExtraction + DataCollection + TextAnalysis + Output
def main():
    
    print("Staring PART A : LOAD DATA")
    # PART A : LOAD DATA
    # ==================

    # Create necessary directories if they don't exist
    if not os.path.exists('downloaded_images'):
        os.makedirs('downloaded_images')

    if not os.path.exists('texts_extracted'):
        os.makedirs('texts_extracted')

    # Initialize PostCollection and EventCollection
    post_collection = PostCollection()
    event_collection = EventCollection()

    # Load posts from JSON
    post_collection.load_from_json(r'impfiles\updated-dataset.json')
    post_collection.show_post_collection()
    
    # Download all images for the posts
    post_collection.download_all_images()
    print("\n")    
    print("PART A Completed")
    print("\n")
    
    # print("Staring PART B : EXTRACT DATA")
    # # PART B : EXTRACT DATA  (OCR Using Google Cloud Vision API)
    # # =====================

    # # Path to your Google Cloud service account credentials JSON file
    # credentials_path = r'impfiles\google-vision-service-account.json'
    
    # # Initialize the GoogleVisionExtractor with the credentials
    # extractor = GoogleVisionExtractor(credentials_path)
    
    # # Path to the folder containing the images you want to process
    # images_folder = 'downloaded_images'
    
    # # Output folder where the extracted text will be saved
    # output_folder = 'texts_extracted'
    
    # # Loop through all the image files in the images folder
    # for image_filename in os.listdir(images_folder):
    #     image_path = os.path.join(images_folder, image_filename)
        
    #     # Ensure that the file is an image (e.g., .jpg, .png)
    #     if image_filename.lower().endswith(('.jpg', '.jpeg', '.png')):
    #         # Extract text from the image and save it
    #         extracted_text = extractor.extract_text_from_image(image_path, output_folder)
    #         # Optionally, print or process the extracted text
    #         print(f"Extracted text from {image_filename}: {extracted_text}\n")
    # post_collection.write_caption_files()
    # print("\n")
    # print("PART B Completed")
    # print("\n")

    

if __name__ == "__main__":
    main()