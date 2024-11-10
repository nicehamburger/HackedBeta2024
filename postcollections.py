import json
from post import Post

class PostCollection:
    def __init__(self):
        self.posts = []

    def load_from_json(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            local_id = 1  # Initialize local ID

            for post_data in data:
                    post_id = "post_" + str(local_id)
                    input_url = post_data.get('inputUrl')
                    url = post_data.get('url')
                    caption = post_data.get('caption')
                    display_url = post_data.get('displayUrl')
                    
                    # Create Post object and add it if not a duplicate
                    new_post = Post(post_id, input_url, url, caption, display_url)
                    self.posts.append(new_post)
                    local_id += 1
                    
        except Exception as e:
            print(f"Error loading data from JSON: {e}")
        print("\n")

    def download_all_images(self):
        for post in self.posts:
            post.download_image()

    def show_post_collection(self):
        if not self.posts:
            print("No posts in the collection.")
        else:
            print(f"Post Collection ({len(self.posts)} posts):")
            for post in self.posts:
                print(post)

    def write_caption_files(self):
        for post in self.posts:
            post.write_caption_to_file()

    def __str__(self):
        return f"PostCollection({len(self.posts)} posts)"