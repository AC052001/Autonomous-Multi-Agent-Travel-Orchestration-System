import requests

OPENWEATHER_API_KEY = "c39dd3ca982094040b315c00f6c4f2b2"

def get_weather(location: str) -> dict:
    """
    Get the current weather for a location using OpenWeatherMap API.
    
    Args:
        location: City or location name
    
    Returns:
        Weather information including temperature, conditions, and humidity
    """
    if not location:
        return {"error": "No location provided"}

    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code != 200:
            return {"error": data.get("message", "Failed to retrieve weather data")}

        temperature_c = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        conditions = data["weather"][0]["description"].capitalize()

        return {
            "location": data["name"],
            "temperature_celsius": temperature_c,
            "temperature_fahrenheit": round((temperature_c * 9 / 5) + 32, 1),
            "conditions": conditions,
            "humidity": humidity,
            "forecast": f"The weather in {data['name']} is currently {conditions.lower()} with a temperature of {temperature_c}°C."
        }

    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {e}"}


