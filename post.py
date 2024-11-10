import os
import requests

class Post:
    def __init__(self, post_id, input_url, url, caption, display_url):
        self.input_url = input_url
        self.url = url
        self.caption = caption
        self.display_url = display_url
        self.post_id = post_id  # Unique identifier for each post

    def download_image(self):
        try:
            response = requests.get(self.display_url)
            if response.status_code == 200:
                image_name = f"{self.post_id}.jpg"  # Image named after the post_id
                image_path = os.path.join('downloaded_images', image_name)
                with open(image_path, 'wb') as img_file:
                    img_file.write(response.content)
                print(f"Image {self.post_id} downloaded successfully!")
            else:
                print(f"Failed to download image {self.post_id}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error downloading image {self.post_id}: {e}")

    def write_caption_to_file(self):
        try:
            # Ensure the 'captions_extracted' folder exists (creates it if not)
            os.makedirs('captions_extracted', exist_ok=True)
            
            # Define the file path with the post ID as the filename
            file_name = f"{self.post_id}.txt"
            file_path = os.path.join('captions_extracted', file_name)
            
            # Write the caption to the file with UTF-8 encoding
            with open(file_path, 'w', encoding='utf-8') as caption_file:
                caption_file.write(self.caption)
            print(f"Caption for post {self.post_id} written to {file_path}")
        except Exception as e:
            print(f"Error writing caption for post {self.post_id}: {e}")

    def __str__(self):
        return f"Post(id={self.post_id}, input_url={self.input_url})"

    def __eq__(self, other):
        return isinstance(other, Post) and self.id == other.id