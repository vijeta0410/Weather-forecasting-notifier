import requests
import datetime as dt

def get_weather(location, API_KEY="7526b7d25f878d54d786266ef0bde69e"):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    url = BASE_URL + "appid=" + API_KEY + "&q=" + location

    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    def kelvin_to_fahrenheit(kelvin):
        return 1.8 * (kelvin - 273.15) + 32

    try:
        response = requests.get(url).json()
        
        if response.get("cod") != 200:  
            print(f"Error fetching weather data: {response.get('message', 'Unknown error')}")
            return None

        formatted_sunrise = dt.datetime.fromtimestamp(
            response['sys']['sunrise'], dt.timezone.utc
        ).strftime("%Y-%m-%d %H:%M:%S")
        formatted_sunset = dt.datetime.fromtimestamp(
            response['sys']['sunset'], dt.timezone.utc
        ).strftime("%Y-%m-%d %H:%M:%S")

        weather = {
            'temp_kelvin': response['main']['temp'],
            'temp_celsius': kelvin_to_celsius(response['main']['temp']),
            'temp_fahrenheit': kelvin_to_fahrenheit(response['main']['temp']),
            'feels_like_kelvin': response['main']['feels_like'],
            'feels_like_celsius': kelvin_to_celsius(response['main']['feels_like']),
            'feels_like_fahrenheit': kelvin_to_fahrenheit(response['main']['feels_like']),
            'wind_speed': response['wind']['speed'],
            'humidity': response['main']['humidity'],
            'description': response['weather'][0]['description'],
            'sunrise_time': formatted_sunrise,
            'sunset_time': formatted_sunset,
        }
        return weather
    except KeyError as e:
        print(f"Key error while processing weather data: {e}")
    except Exception as e:
        print(f"Unexpected error while fetching weather data: {e}")
    return None

