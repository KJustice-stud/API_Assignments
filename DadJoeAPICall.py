import requests

def get_dad_joke():
    # The API endpoint URL
    url = 'http://icanhazdadjoke.com'

    # The header required by the API
    headers = {
        'Accept': 'application/json',
    }

    # Sending the GET request to the API endpoint
    response = requests.get(url, headers=headers)

    # Checking if the request was successful
    if response.status_code == 200:
        # If successful, parse the JSON response and return the joke text
        return response.json()['joke']
    else:
        # If unsuccessful, return a message indicating the error
        return 'Failed to retrieve joke. HTTP Response Code: ' + str(response.status_code)

# Printing out a dad joke
print("Here's a random dad joke for you:")
print(get_dad_joke())
