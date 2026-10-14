
import requests

API_KEY = "YOUR_OPENWEATHER_API_KEY"

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if response.status_code != 200:
            print("Error:", data.get("message", "Unable to fetch weather"))
            return

        print("\n========== WEATHER REPORT ==========")
        print("City:", data["name"])
        print("Country:", data["sys"]["country"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Feels Like:", data["main"]["feels_like"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"].title())
        print("Wind Speed:", data["wind"]["speed"], "m/s")
        print("====================================")

    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")

def get_forecast(city):
    url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if response.status_code != 200:
            print("Forecast error:", data.get("message", "Unable to fetch forecast"))
            return

        print("\n======= UPCOMING FORECAST =======")

        for item in data["list"][:5]:
            print("\nDate and Time:", item["dt_txt"])
            print("Temperature:", item["main"]["temp"], "°C")
            print("Humidity:", item["main"]["humidity"], "%")
            print("Condition:", item["weather"][0]["description"].title())

        print("\n=================================")

    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")

def main():
    print("================================")
    print("       LIVE WEATHER APP")
    print("================================")

    while True:
        city = input("\nEnter city name (or 'exit' to quit): ").strip()

        if city.lower() == "exit":
            print("Thank you for using the Weather App!")
            break

        if not city:
            print("Please enter a city name.")
            continue

        get_weather(city)
        get_forecast(city)

if __name__ == "__main__":
    main()
