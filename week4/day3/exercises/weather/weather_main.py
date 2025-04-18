from weather_services import *

def print_weather(info):
    print(f"\nWeather: {info['status']}")
    print(f"Temp: {info['temp']}°C")
    print(f"Wind: {info['wind']}")
    print(f"Sunrise: {info['sunrise']}")
    print(f"Sunset: {info['sunset']}")

def print_forecast(forecasts):
    print("\nForecast:")
    for item in forecasts:
        print(f"{item['time']} | {item['status']} | {item['temp']}°C")

def main():
    while True:
        print("\n Menu:")
        print("1. The weather in TLV")
        print("2. The weather in a dif city")
        print("3. Forecast by city ID")
        print("4. The air quality by coordinates")
        print("5. Quit")

        choice = input("Choose: ")

        if choice == '1':
            data = get_weather_by_city("Tel Aviv,IL")
            print_weather(data)

        elif choice == '2':
            city = input("Enter a city name (for example, London,GB): ")
            try:
                data = get_weather_by_city(city)
                print_weather(data)
            except:
                print("The city isnt found.")

        elif choice == '3':
            city = input("Enter a city name: ")
            city_id = get_city_id(city)
            if city_id:
                forecasts = get_forecast_by_id(city_id)
                print_forecast(forecasts)
            else:
                print("The ID isnt found.")

        elif choice == '4':
            try:
                lat = float(input("Enter lat: "))
                lon = float(input("Enter lon: "))
                aqi = get_air_quality(lat, lon)
                print(f"\nAir quality index (AQI): {aqi}")
            except:
                print("Coordinate enter error.")

        elif choice == '5':
            print("Bye!")
            break
        else:
            print("Wrong choice.")

if __name__ == "__main__":
    main()
