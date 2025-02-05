import requests
import os
from dotenv import load_dotenv
from fastapi import HTTPException


load_dotenv()
COOKIE_API_KEY = os.getenv("COOKIE_API_KEY")
BASE_URL = "https://api.cookie.fun"

def fetch_from_cookie_api(endpoint: str, params: dict = None):
    headers = {"x-api-key": COOKIE_API_KEY}
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}", headers=headers, params=params)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  
        raise HTTPException(status_code=response.status_code, detail=f"HTTP error: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")  
        raise HTTPException(status_code=500, detail="An error occurred while fetching data from the Cookie API.")
