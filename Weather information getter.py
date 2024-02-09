import requests

def get_destination_weather(destination, api_key):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': destination, 'appid': api_key}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_info = response.json()
        return weather_info
    else:
        print(f"Error: {response.status_code}")
        return None

# Example usage:
user_destination = input("Enter your destination: ")
user_api_key = 'Use your own API key' # Replace with your actual API key

weather_info = get_destination_weather(user_destination, user_api_key)

if weather_info:
    print("Weather Information:")
    print(weather_info)
else:
    print("Failed to retrieve weather information.")
