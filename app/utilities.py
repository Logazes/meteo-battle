import requests

def get_city(city_name, country, api_key, limit=5):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": f"{city_name}, {country}",
        "limit": limit,
        "appid": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None