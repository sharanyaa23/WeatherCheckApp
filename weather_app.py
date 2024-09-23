import requests

# OpenWeatherMap API key
api_key = "01ab1ec206859d82eaaa675d764f011c"

# Base URL 
base_url = "http://api.openweathermap.org/data/2.5/weather?"


city_name = input("Enter city name: ")

# complete url
complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

response = requests.get(complete_url)

data = response.json()

if response.status_code == 200:
    
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']} °C")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")
else:
    print("City not found. Please check the city name.")
