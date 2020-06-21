import requests
from pprint import pprint

response = requests.get(
    "https://api.meraki.com/api/v0/organizations/549236/networks",
    headers={"X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"},
)

pprint(response.json())

