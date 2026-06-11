import os

import requests


def get_weather(city):
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("API_KEY is missing")
        return None

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

    try:
        response = requests.get(url, timeout=10)
        print("Status:", response.status_code)
        print("Response:", response.text)

        if response.status_code == 200:
            return response.json()
    except requests.RequestException as exc:
        print("Request error:", exc)

    return None