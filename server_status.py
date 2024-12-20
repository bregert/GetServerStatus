import requests

url = "https://github.com/bregert"

def check_server_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Server is up! Status Code: {response.status_code}")
        else:
            print(f"Server returned an error. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = "https://github.com/bregert"
    check_server_status(url)
