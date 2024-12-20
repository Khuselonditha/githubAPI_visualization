# imports
import requests

# Make an API call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=launguage:python+sort:stars+stars:>1000"

headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers)
print(f"Status code: {response.status_code}")

# Convert the response to a dictionary
response_dict = response.json()

# Print the response
print(response_dict.keys())