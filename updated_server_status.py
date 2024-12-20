import requests

url = input("What server do you want to check? ")

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"The server at {url} is up and running.")
    else:
        print(f"The server at {url} returned a status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
