import anvil.server
import requests 

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42

@anvil.server.callable
def save_image(image_base64, filename):
    # Define the URL of your FastAPI endpoint
    fastapi_endpoint = "http://127.0.0.1:8000/save_image"
  # Line added to trobleshoot  
    # Print the FastAPI endpoint to verify the URL
    print(fastapi_endpoint)  # Check the endpoint URL

    # Print the first 50 characters of the Base64-encoded image to verify encoding
    print(image_base64[:50])  # Preview the Base64 encoding
      
    # Send the data to your FastAPI app
    response = requests.post(fastapi_endpoint, json={
        "image_base64": image_base64,
        "filename": filename
    })
    
    # Check if the response is successful
    if response.status_code == 200:
        return response.json()
    else:
        return {"status": "error"}
