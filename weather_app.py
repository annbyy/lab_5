from weather_utils import get_weather, format_weather

def main():
    city = input("Name of city: ")
    weather_data = get_weather(city)

    if "cod" in weather_data and weather_data["cod"] == "404":
        print("City is not found.")
    else:
        formatted_weather = format_weather(weather_data)
        print(formatted_weather)

if __name__ == "__main__":
    main()
