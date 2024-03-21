import requests

def get_weather(location, units):
    api_key = "YOUR_API_KEY"  # Replace with your API key from OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units={units}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data.")
        return None

def display_weather(weather_data, units):
    if weather_data:
        print("Weather Forecast:")
        print(f"Location: {weather_data['name']}, {weather_data['sys']['country']}")
        if units == 'metric':
            print(f"Temperature: {weather_data['main']['temp']}°C")
            print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        elif units == 'imperial':
            print(f"Temperature: {weather_data['main']['temp']}°F")
            print(f"Wind Speed: {weather_data['wind']['speed']} mph")
        else:
            print("Invalid unit selection.")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Weather: {weather_data['weather'][0]['description']}")
    else:
        print("Weather data unavailable.")

def main():
    location = input("Enter city name or zip code: ")
    units = input("Enter preferred units (metric/imperial): ").lower()
    while units not in ['metric', 'imperial']:
        print("Invalid units. Please enter 'metric' or 'imperial'.")
        units = input("Enter preferred units (metric/imperial): ").lower()
    weather_data = get_weather(location, units)
    display_weather(weather_data, units)

if __name__ == "__main__":
    main()