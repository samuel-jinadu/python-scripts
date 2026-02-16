print("Importing required libraries...", "\n")
import requests, json, time
from openweathermapAPI import API_key

print("Imported required libraries.", 2*"\n")

# get  geo-coordinates

def handle_error(error = ""):
	print(error)
	input()
	exit()

def notification(weather):
	success = False
	while not success:
		response = requests.post('https://ntfy.sh/AlSweigartZPgxBQ42', f"Weather is: '{weather}'", timeout=10)
		success = response.ok
		time.sleep(5)
	else:
		print("Notification of rain sent!")
		handle_error()

def get_weather_ibadan():
	CITY = "Ibadan"
	try:
		response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={CITY}&appid={API_key}')
		if response.ok:
			lat = json.loads(response.text)[0]['lat']
			lon = json.loads(response.text)[0]['lon']
			response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}')
			if response.ok:
				response_data = json.loads(response.text)
				weather = response_data["weather"][0]["description"]
				return weather
			else:
				handle_error(f"Error: {response.status_code}")
		else:
			handle_error(f"Error: {response.status_code}")
	
	except Exception as e:
		handle_error(e)

notification(get_weather_ibadan())