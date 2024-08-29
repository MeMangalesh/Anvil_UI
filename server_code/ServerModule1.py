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
    
    # Send a request to the FastAPI endpoint
    response = requests.post(
        fastapi_endpoint,
        json={"image_base64": image_base64, "filename": filename}
    )
    
    # Return the response from the FastAPI server
    return response.json()
    
    # Check if the response is successful
    if response.status_code == 200:
        return response.json()
    else:
        return {"status": "error"}
