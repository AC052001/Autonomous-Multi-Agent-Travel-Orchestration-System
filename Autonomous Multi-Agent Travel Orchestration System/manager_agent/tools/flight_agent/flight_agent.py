"""
Flight Radar Tool
------------------
Fetches live flight data (status, delays, etc.) using FlightRadar24 API (demo mock).

Usage:
    from manager_agent.tools.flight_radar_tool.agent import get_flight_status
    result = get_flight_status("AI302")
"""

import os
import requests

FLIGHTRADAR_API_KEY = os.getenv("FLIGHTRADAR_API_KEY", "demo_flight_key")
FLIGHTRADAR_URL = "https://example-flightradar-api.com/status"

def get_flight_status(flight_number: str):
    try:
        if FLIGHTRADAR_API_KEY == "demo_flight_key":
            return {
                "flight": flight_number,
                "status": "On Time",
                "departure": "New Delhi (DEL)",
                "arrival": "London Heathrow (LHR)",
                "departure_time": "23:40 IST",
                "arrival_time": "05:55 GMT",
            }
        params = {"flight": flight_number}
        headers = {"x-api-key": FLIGHTRADAR_API_KEY}
        response = requests.get(FLIGHTRADAR_URL, params=params, headers=headers, timeout=10)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
