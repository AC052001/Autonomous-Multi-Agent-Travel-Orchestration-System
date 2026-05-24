"""
Hotel Agent
-----------------
Fetches and recommends hotels based on user’s destination, budget, and rating preferences.
Integrates with Booking.com / RapidAPI style endpoint (mocked for demo).

Usage:
    from manager_agent.sub_agents.hotel_agent.agent import hotel_agent
    result = hotel_agent("Paris", budget=12000)
"""

import requests
import os

# Demo API key (replace with your real key later)
HOTEL_API_KEY = os.getenv("HOTEL_API_KEY", "demo_hotel_api_key")
HOTEL_API_URL = "https://example-booking-api.com/search"

def hotel_agent(destination: str, budget: float = 10000, rating: float = 3.5):
    try:
        if HOTEL_API_KEY == "demo_hotel_api_key":
            # Mock response for offline testing
            return {
                "destination": destination,
                "hotels": [
                    {"name": "Hotel Lumiere", "price": 9500, "rating": 4.2},
                    {"name": "Comfort Inn", "price": 8700, "rating": 3.8},
                    {"name": "Grand Stay", "price": 11200, "rating": 4.5},
                ]
            }
        params = {"destination": destination, "budget": budget, "rating": rating}
        headers = {"x-api-key": HOTEL_API_KEY}
        response = requests.get(HOTEL_API_URL, params=params, headers=headers, timeout=10)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
