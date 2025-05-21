import requests
import json

# Define city name for direct script execution
CITY_NAME = "Suzhou"

def get_weather_internal(region_name):
    """
    Get weather information for the specified city or region
    Uses wttr.in service, a free weather API that doesn't require an API key
    
    Args:
        region_name (str): Name of the region to get weather for.
        
    Returns:
        dict: A dictionary containing weather information
    """
    if not region_name:
        return {"error": "Region name cannot be empty"}
        
    try:
        url = f"https://wttr.in/{region_name}?format=j1"
        response = requests.get(
            url, 
            headers={"User-Agent": "Mozilla/5.0"}, 
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch weather data: {str(e)}"}


def print_weather_info(weather_data):
    """
    Print raw weather data directly
    """
    if isinstance(weather_data, dict) and "error" in weather_data:
        print(f"Error: {weather_data['error']}")
        return
    
    # Print the raw weather data
    print(json.dumps(weather_data, indent=2, ensure_ascii=False))

# When this file is run directly, get and print weather information
if __name__ == "__main__":
    weather_info = get_weather_internal(CITY_NAME)
    print_weather_info(weather_info)
