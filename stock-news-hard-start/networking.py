import requests


def send_tsla_request():
    # Alphavantage
    # GET https://www.alphavantage.co/query

    try:
        response = requests.get(
            url="https://www.alphavantage.co/query",
            params={
                "apikey": "9O8EFR0TTQGJNMNX",
                "function": "TIME_SERIES_DAILY",
                "symbol": "TSLA",
            },
            headers={
                "Cookie": "__cfduid=d72c6f1eee528d3afd218fe02b64cf8e51619882104",
            },
        )

        return response.json()
    except requests.exceptions.RequestException:
        print('HTTP Request failed')