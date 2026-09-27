import os
from dotenv import load_dotenv
from django.shortcuts import render
import requests

# Load environment variables from .env file
load_dotenv()

# Replace with your actual API key
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def index(request):
    city = ""
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.POST.get("city", "").strip()
        if city:
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric",  # Celsius
            }
            try:
                response = requests.get(BASE_URL, params=params, timeout=5)
                response.raise_for_status()
                data = response.json()

                # OpenWeatherMap returns "cod": "404" if city not found
                if data.get("cod") != 200:
                    error = "City not found. Please check the spelling."
                else:
                    weather_data = {
                        "city": data["name"],
                        "country": data["sys"]["country"],
                        "temp": data["main"]["temp"],
                        "feels_like": data["main"]["feels_like"],
                        "humidity": data["main"]["humidity"],
                        "description": data["weather"][0]["description"].capitalize(),
                        "icon": data["weather"][0]["icon"],
                    }
            except requests.exceptions.RequestException:
                error = "Failed to fetch weather. Check your internet connection."

    context = {
        "city": city,
        "weather_data": weather_data,
        "error": error,
    }
    return render(request, "index.html", context)