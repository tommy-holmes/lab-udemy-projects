import requests

def send_request():
    # Request
    # GET https://api.openweathermap.org/data/2.5/onecall

    try:
        response = requests.get(
            url="https://api.openweathermap.org/data/2.5/onecall",
            params={
                "lat": "51.51",
                "lon": "-0.13",
                "exclude": "current,minutely,daily,alerts",
                "appid": "0d360b543e83bfaa3d62cdcb5f1ec4a2",
            },
        )
        return response.json()['hourly']

    except requests.exceptions.RequestException:
        print('HTTP Request failed')