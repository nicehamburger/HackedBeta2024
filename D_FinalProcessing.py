import re

# Sample input text (replace this with your file reading logic)
with open("response.txt", "r") as reader:
    input_text = reader.read()

# Define a function to process the input text and generate the output file
def extract_all_events(input_text):
    # Split the text into blocks, each starting with "post_"
    event_blocks = input_text.split("post_")[1:]  # Ignore the first empty part
    
    # Open the output text file to write results
    with open('all_events.txt', 'w') as outfile:
        for block in event_blocks:
            # Use regex to capture each piece of information from the event block
            event_name = re.search(r'Event Name:\s*(.*?)\n', block)
            date = re.search(r'Date:\s*(.*?)\n', block)
            time = re.search(r'Time:\s*(.*?)\n', block)
            location = re.search(r'Location:\s*(.*?)\n', block)
            food = re.search(r'Food:\s*(.*?)\n', block)
            registration_fee = re.search(r'Registration/Entry fee:\s*(.*?)\n', block)
            
            # If all pieces of information are found, write them to the file
            if event_name and date and time and location and food and registration_fee:
                event_details = {
                    'post_number': f"post_{event_blocks.index(block) + 1}",
                    'Event Name': event_name.group(1),
                    'Date': date.group(1),
                    'Time': time.group(1),
                    'Location': location.group(1),
                    'Food': food.group(1),
                    'Registration/Entry fee': registration_fee.group(1),
                }
                # Write the event information to the file
                outfile.write(f"post_number: {event_details['post_number']}\n")
                outfile.write(f"Event Name: {event_details['Event Name']}\n")
                outfile.write(f"Date: {event_details['Date']}\n")
                outfile.write(f"Time: {event_details['Time']}\n")
                outfile.write(f"Location: {event_details['Location']}\n")
                outfile.write(f"Food: {event_details['Food']}\n")
                outfile.write(f"Registration/Entry fee: {event_details['Registration/Entry fee']}\n")
                outfile.write("\n--------------------------\n")

# Run the function to process the input and save results to the file
extract_all_events(input_text)
