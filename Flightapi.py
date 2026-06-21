import requests
import os

API_KEY = os.getenv("SERPAPI_KEY")
print("API Key:", API_KEY)
url = "https://serpapi.com/search.json"

params = {
    "engine": "google_flights",
    "departure_id": "BLR",
    "arrival_id": "DEL",
    "outbound_date": "2026-06-22",
    "return_date": "2026-06-30",
    "currency": "INR",
    "hl": "en",
    "api_key": API_KEY
}

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()

best_flights = data.get("best_flights", [])

if best_flights:
    cheapest = best_flights[0]
    print("Price:", cheapest["price"])
    print("Successful!")
else:
    print("No flights found.")