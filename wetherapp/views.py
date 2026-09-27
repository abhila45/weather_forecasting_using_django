import os
from dotenv import load_dotenv
from django.shortcuts import render
from django.http import JsonResponse
import requests
from datetime import datetime, timedelta

# Load environment variables from .env file
load_dotenv()

# Replace with your actual API key
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
GEO_URL = "https://api.openweathermap.org/geo/1.0/direct"

# Popular world cities for the dropdown
POPULAR_CITIES = [
    "New York", "London", "Tokyo", "Paris", "Sydney",
    "Dubai", "Singapore", "Hong Kong", "Los Angeles", "Chicago",
    "Toronto", "Mumbai", "Shanghai", "Beijing", "Seoul",
    "Berlin", "Rome", "Madrid", "Amsterdam", "Barcelona",
    "Moscow", "Istanbul", "Bangkok", "Jakarta", "Manila",
    "Sao Paulo", "Mexico City", "Buenos Aires", "Cairo", "Lagos",
    "Bhubaneswar", "Delhi", "Bangalore", "Mumbai", "Chennai"
]

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
                    # Calculate local time using timezone offset
                    timezone_offset = data.get("timezone", 0)  # in seconds
                    utc_time = datetime.utcnow()
                    local_time = utc_time + timedelta(seconds=timezone_offset)
                    
                    weather_data = {
                        "city": data["name"],
                        "country": data["sys"]["country"],
                        "temp": data["main"]["temp"],
                        "feels_like": data["main"]["feels_like"],
                        "humidity": data["main"]["humidity"],
                        "description": data["weather"][0]["description"].capitalize(),
                        "icon": data["weather"][0]["icon"],
                        "local_time": local_time.strftime("%I:%M %p"),
                        "local_date": local_time.strftime("%A, %B %d, %Y"),
                    }
            except requests.exceptions.RequestException:
                error = "Failed to fetch weather. Check your internet connection."

    context = {
        "city": city,
        "weather_data": weather_data,
        "error": error,
        "popular_cities": POPULAR_CITIES,
    }
    return render(request, "index.html", context)


def city_autocomplete(request):
    """API endpoint for city autocomplete suggestions"""
    query = request.GET.get('q', '').strip()
    
    if not query or len(query) < 2:
        return JsonResponse({'suggestions': []})
    
    try:
        # Use OpenWeatherMap Geocoding API for city suggestions
        params = {
            'q': query,
            'limit': 5,
            'appid': API_KEY
        }
        response = requests.get(GEO_URL, params=params, timeout=3)
        response.raise_for_status()
        data = response.json()
        
        suggestions = []
        for city in data:
            city_name = city.get('name', '')
            country = city.get('country', '')
            state = city.get('state', '')
            
            # Format the suggestion like Google does
            if state:
                display_name = f"{city_name}, {state}, {country}"
            else:
                display_name = f"{city_name}, {country}"
            
            suggestions.append({
                'name': city_name,
                'display_name': display_name,
                'country': country,
                'state': state
            })
        
        return JsonResponse({'suggestions': suggestions})
        
    except requests.exceptions.RequestException:
        return JsonResponse({'suggestions': []})