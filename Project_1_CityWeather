import requests
# from datetime import datetime
# import pytz

API_KEY = "e062b31baa7a4b5ae86585e45a1c6a8e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

print("\n\n********** KNOW YOUR CITY **********")

city = input("Enter a city name: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    coord1 = data['coord']['lon']
    coord2 = data['coord']['lat']
    temperature = round(data['main']['temp'] - 273.15, 2)
    humidity = data['main']['humidity']
    windSpeed = data['wind']['speed']
    noOfClouds = data['clouds']['all']
    country = data['sys']['country']
    cityName = data['name']

    # dateTime = datetime.now(pytz.timezone('Asia/Kolkata'))

    print("\n***** Here's your City's Weather Info *****\n")

    print("City Name:", cityName)
    print("Country Code:", country)
    print(f"Coordinates of {city}: {coord1, coord2}")
    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
    print("Humidity:", humidity)
    print("Wind Speed:", windSpeed, "m/s")
    print("No. of Clouds:", noOfClouds)

    print("\n*****__________________*****\n")

    # print("Date and Time:", dateTime)

else:
    print("An error occurred.")
