import os
import requests
import json

# Define API endpoint
api_url = "http://localhost:4891/v1/chat/completions"

# Define the folder paths
captions_folder = "captions_extracted"
texts_folder = "texts_extracted"

# Number of posts to process
num_posts = 25

# Loop through each post
for idx in range(1, num_posts + 1):
    caption_file = os.path.join(captions_folder,f"post_{idx}.txt")
    text_file = os.path.join(texts_folder, f"post_{idx}.txt")

    # Check if both files exist
    if os.path.exists(text_file):
        # Read the contents of the files
        with open(caption_file, 'r', encoding='utf-8') as cf:
            caption_list = cf.readlines()
            caption_content = ""
            for i in caption_list:
                caption_content += i + " "
        with open(text_file, 'r', encoding='utf-8') as tf:
            text_list = tf.readlines()
            text_content = " "
            for i in text_list:
                text_content += i + " "

        # Construct the message for the API
        message = f"""
        Extract the following details from Caption and Text:
        Event Name: (As given)
        Date: (Simple format)
        Time: (Simple format)
        Location: (As given)
        Food: Yes/Not Specified

        Text:{text_content}
        """

        # Create the payload for the API request
        payload = {
            "model": "Phi-3 Mini Instruct",
            "messages": [{"role": "user", "content": message}],
            "max_tokens": 100,
            "temperature": 0.28
        }

        # Make the API request
        try:
            response = requests.post(api_url, headers={"Content-Type": "application/json"}, data=json.dumps(payload))
            
            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                json_response = response.json()
                output = json_response.get("choices", [{}])[0].get("message", {}).get("content", "")

                if output:
                    with open('response.txt', 'a') as file:
                        file.write(f"post_{idx}\n")
                        file.write(output.strip() + "\n--------------------------\n")
                else:
                    print(f"Post_{idx}: No content extracted")

                # Display the output
                print(f"Post_{idx}:")
                print(output.strip())
                print("--------------------------")
                # Clear the output variable
                output = ""
            else:
                print(f"Post_{idx}: API request failed with status code {response.status_code}")
            cf.close()
            tf.close()

        except Exception as e:
            print(f"Post_{idx}: Error occurred - {str(e)}")
    else:
        print(f"Post_{idx}: Missing files in one of the folders.")
