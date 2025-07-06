import requests
from datetime import datetime

def fetch_real_time_data():
    # Use dummy ship coordinates for now
    lat, lon = 18.944, 72.835  # Mumbai coast

    try:
        weather_resp = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m")
        weather_data = weather_resp.json()["current"]
    except:
        weather_data = {"temperature_2m": 30, "wind_speed_10m": 10}

    return {
        "lat": lat,
        "lon": lon,
        "weather": f"{weather_data['temperature_2m']}°C, {weather_data['wind_speed_10m']} kn",
        "timestamp": datetime.now().isoformat()
    }