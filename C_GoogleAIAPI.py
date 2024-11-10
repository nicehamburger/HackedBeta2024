import google.generativeai as genai
import os

# Set the API key directly
API_KEY = "AIzaSyBPsldxB48S-QGAT-vLsd9aLFhIWWGDulk"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

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
    if os.path.exists(caption_file) and os.path.exists(text_file):
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
        message = f'''
        post_{idx}
        {text_content}
        {caption_content}
        DO THE TEXT PARSING FOR ABOVE TEXTS
        Extract the following details:
        post_number.txt
        Event Name: (As given)
        Date: (Simple format) 
        Time: (Simple format) 
        Location: (As given) 
        Food: Yes/Not Specified
        Registration/Entry fee: (As given)

        Do not write (As given) or (Simple format).
        Be consistent with data output format
        SAMPLE OUTPUT:
        
        Event Name: Hackathon
        Date: November 7
        Time: 11 AM 
        Location: DICE
        Food: Not Specified
        Registration/Entry fee: Unknown
        '''
        response = model.generate_content(message)
        try:
            with open('response.txt', 'a') as file:
                file.write(f"post_{idx}\n")
                file.write(response.text + "\n--------------------------\n")
        
        except:
            print(f"Post_{idx}: No content extracted")

        # Display the output
        print(f"Post_{idx}:")
        print(response.text)
        print("\n")
        print("--------------------------")
        # Clear the output variable
        output = ""
    else:
        print(f"Post_{idx}: API request failed with status code {response.status_code}")
    cf.close()
    tf.close()

print(response.text)