import urllib

# Set the URL to the Backend 
url = "http://192.168.1.69:8000"

print("SymbianGPT - GPT Client Script on Python for S60")

while True:
    userinput = raw_input("User: ")
    # Create a dictionary of form data
    form_data = {
        'prompt': userinput,
    }

    # Encode the form data
    encoded_data = urllib.urlencode(form_data)

    # Make the POST request
    response_data = urllib.urlopen(url, encoded_data).read()

    # Print the response
    print("")
    print("AI: " + response_data)
    print("")
