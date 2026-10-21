import requests
import argparse

class Brewery:
    def __init__(self, data: dict):
        self.id: str = data["id"]
        self.name: str = data["name"]
        self.brewery_type: str = data["brewery_type"]
        self.city: str = data["city"]
        self.country: str = data["country"]
        self.website_url: str | None = data["website_url"]
        
    def __str__(self):
        return f"{self.name} ({self.brewery_type}) - {self.city}, {self.country}"
    
    
parser = argparse.ArgumentParser()
parser.add_argument("--city", type=str)

args = parser.parse_args()
city = args.city


url = f"https://api.openbrewerydb.org/v1/breweries?by_city={city}"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    breweries = [Brewery(brewery_data) for brewery_data in data]
    for brewery in breweries:
        print(brewery)