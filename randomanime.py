# Import library
import requests
from animelist_1 import api_token

# Initialize variables (GET:suggestion anime)
base_url = 'https://api.myanimelist.net/v2/anime/suggestions?limit=4'
headers = {'Authorization': 'Bearer ' + api_token}

# Make the initial request
anime_suggestions = requests.get(base_url, headers=headers)

response = anime_suggestions.json()

#extract title only
for suggestion in response['data']:
    title = suggestion['node']['title']
    print(title)