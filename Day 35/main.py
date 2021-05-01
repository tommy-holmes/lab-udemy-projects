import networking

weather_data = networking.send_request()

for data in weather_data['hourly'][:12]:
    id = data['weather']['id']
    if id > 700:
        print('Bring an umbrella')
