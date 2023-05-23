import requests

URL = "http://localhost:3001/lead"


def send_post_request(data: dict):
    try:
        response = requests.post(URL, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
