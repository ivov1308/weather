from geopy.geocoders import Nominatim
from typing import NamedTuple

from config import USE_ROUNDED_COORDS

class Coordinates(NamedTuple):
    latitude: float
    longitude: float

def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using device GPS"""
    nominatim = Nominatim(user_agent='user')
    location = nominatim.geocode('Saint-Petersburg, Russia').raw
    latitude = float(location['lat'])
    longitude = float(location['lon'])
    if USE_ROUNDED_COORDS:
        latitude, longitude = map(lambda c: round(c, 1), [latitude, longitude])
    return Coordinates(latitude=latitude, longitude=longitude)


if __name__ == "__main__":
    print(get_gps_coordinates())
