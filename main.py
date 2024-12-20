# imports
import requests

# Make an API call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>1000"

headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers)
print(f"Status code: {response.status_code}")

# Convert the response to a dictionary
response_dict = response.json()

# Print the response
print(response_dict.keys())

# Print the total number of repositories
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explore information about the repositories
repo_dict = response_dict["items"]
print(f"Repositories returned: {len(repo_dict)}")