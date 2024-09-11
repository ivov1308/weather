import asyncio
import winsdk.windows.devices.geolocation as wdg
from typing import NamedTuple

from config import USE_ROUNDED_COORDS
from exceptions import CantGetCoordinates


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using device GPS"""
    coordinates = _get_loc()
    return _round_coordinates(coordinates)

def _get_loc() -> Coordinates:
    try:
        return asyncio.run(_get_coords())
    except PermissionError:
        raise CantGetCoordinates

async def _get_coords() -> Coordinates:
    locator = wdg.Geolocator()
    pos = await locator.get_geoposition_async()
    return Coordinates(
        latitude=pos.coordinate.latitude,
        longitude=pos.coordinate.longitude
    )

def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not USE_ROUNDED_COORDS:
        return coordinates
    return Coordinates(*map(
        lambda c: round(c, 1),
        [coordinates.latitude, coordinates.longitude]
    ))


if __name__ == "__main__":
    print(get_gps_coordinates())
