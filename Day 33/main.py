import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

iss_position = (longitude, latitude)


def iss_near(lng=MY_LONG, lat=MY_LAT):
    if MY_LONG - 5 <= lng <= MY_LONG + 5 and MY_LAT - 5 <= lat <= MY_LAT + 5:
        return True
    else:
        return False


position = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

sun_response = requests.get("https://api.sunrise-sunset.org/json", params=position)
sun_response.raise_for_status()
sun_data = sun_response.json()
sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour_now = time_now.hour

# If the ISS is close to me
# and it is currently dark
if iss_near() and sunset <= hour_now <= sunrise:
    # then tell me to look up
    print("Look Up")
