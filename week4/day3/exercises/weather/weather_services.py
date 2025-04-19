from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from datetime import datetime

API_KEY = '///'  

config_dict = get_default_config()
config_dict['language'] = 'en'

owm = OWM(API_KEY, config_dict)
mgr = owm.weather_manager()
air_mgr = owm.airpollution_manager()
registry = owm.city_id_registry()

def get_weather_by_city(city_name):
    observation = mgr.weather_at_place(city_name)
    weather = observation.weather
    return {
        'status': weather.detailed_status,
        'temp': weather.temperature('celsius')['temp'],
        'wind': weather.wind(),
        'sunrise': datetime.utcfromtimestamp(weather.sunrise_time()).strftime('%H:%M:%S'),
        'sunset': datetime.utcfromtimestamp(weather.sunset_time()).strftime('%H:%M:%S')
    }

def get_city_id(city_name):
    location = registry.locations_for(city_name)
    if location:
        return location[0].id
    return None

def get_forecast_by_id(city_id):
    forecast = mgr.forecast_at_id(city_id, '3h')
    forecasts = []
    for w in forecast.forecast.weathers[:5]:  
        forecasts.append({
            'time': w.reference_time('iso'),
            'status': w.detailed_status,
            'temp': w.temperature('celsius')['temp']
        })
    return forecasts

def get_air_quality(lat, lon):
    air = air_mgr.air_quality_at_coords(lat, lon)
    return air.aqi
