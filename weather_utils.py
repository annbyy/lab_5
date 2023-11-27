import requests

def get_weather(city):

    api_key = "ff188543251e1dd98f0e91d663b56cef"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": api_key,
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    return weather_data

def format_weather(weather_data):

    if "cod" in weather_data and weather_data["cod"] == "404":
        return "City is not found."

    try:
        main_info = weather_data["weather"][0]["main"]
        description = weather_data["weather"][0]["description"]
        temperature_kelvin = weather_data["main"]["temp"]

        temperature_celsius = temperature_kelvin - 273.15

        formatted_weather = f"Now in the city {weather_data['name']} {main_info} ({description}) and temperature is {temperature_celsius:.2f}°C."
        return formatted_weather
    except KeyError:
        return "Error."
