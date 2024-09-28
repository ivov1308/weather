from pathlib import Path

from coordinates_win import get_gps_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather
from exceptions import CantGetCoordinates, ApiServiceError
from history import save_weather, JSONFileWeatherStorage


def main():
    try:
        coordinates = get_gps_coordinates()
    except CantGetCoordinates:
        print("Не удалось получить GPS координаты")
        raise exit(1)
    try:
        weather = get_weather(coordinates)
    except ApiServiceError:
        print(f"Не удалось получить погоду от сервиса погоды")
        raise exit(1)
    print('\n'+format_weather(weather))

    save_weather(
        weather,
        JSONFileWeatherStorage(Path.cwd() / "history.json")
    )


if __name__ == "__main__":
    input("Получить текущую погоду -> [Enter]")
    print("Выполняется. Ждите...")
    main()
    print("Завершено.")
    input("Выйти -> [Enter]")
