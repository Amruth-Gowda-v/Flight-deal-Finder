# Flight Deal Finder

A Python desktop interface that displays a flight price returned by SerpApi's Google Flights search engine.

## Features

- Requests flight-search data from SerpApi
- Reads the best-flight result from the API response
- Displays the returned price in a Tkinter window

## Requirements

- Python 3
- `requests`
- A SerpApi API key

Install the dependency:

```bash
python -m pip install requests
```

## Configuration

Set your SerpApi key as an environment variable named `SERPAPI_KEY`.

The route, travel dates, currency, and language are currently configured in `Flightapi.py`. Update them there before making a new search. The current dates in the source are historical and should be replaced.

## Run

```bash
python main.py
```

Run the program from the repository directory so that Python can import `Flightapi.py`.

## Notes

- The application depends on a working SerpApi account and available API quota.
- The current implementation expects a best-flight result in the API response. If the API returns no matching flights, the source may need additional handling.
