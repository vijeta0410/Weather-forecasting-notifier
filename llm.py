from langchain_ollama import OllamaLLM
from weather import get_weather
from langchain.globals import set_verbose


set_verbose(False)
def generate_message(username, weather, language):
    # Use the updated OllamaLLM class
    llama = OllamaLLM(model="llama2")

    prompt = f"""
You are a friendly and cheerful weather reporter providing personalized weather updates. Write an engaging and easy-to-read message for {username} in {language}. Use a friendly tone, include emojis, and make the message helpful and fun.

Weather Details:
- 🌡️ Temperature: {weather['temp_celsius']}°C ({weather['temp_fahrenheit']}°F)
- Feels like: {weather['feels_like_celsius']}°C ({weather['feels_like_fahrenheit']}°F)
- 🌤️ Condition: {weather['description']}
- 💨 Wind speed: {weather['wind_speed']} km/h
- 💧 Humidity: {weather['humidity']}%
- 🌅 Sunrise: {weather['sunrise_time']}
- 🌇 Sunset: {weather['sunset_time']}

Based on the weather:
1. **Weather Summary**: Decribe about the temperature, feels like, condition, wind speed, humidity sunrise and sunset time at the location mentioning the location name
2. 🚶‍♂️ **Precautions**: Suggest how to stay safe in this weather.
3. 🚗 **Transportation Advice**: Recommend the best mode of transportation (e.g., walking, public transport, etc.).
4. 👗 **Clothing**: Recommend the type of clothing to wear.
5. 🍲 **Food**: Suggest suitable food or drinks to enjoy in this weather.
6. 🎉 **Activities**: Suggest fun activities to do based on the conditions.
7. ❤️ **Health Tips**: Include health tips to ensure safety and well-being.

End the message with a cheerful note, and ensure it's easy to understand and relatable.
"""

    message = llama.invoke(prompt)
    return message
