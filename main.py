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

# Examine the first repository
first_repo = repo_dict[0]
# print(f"\nKeys: {len(first_repo)}")
# for key in sorted(first_repo.keys()):
#     print(key)

# Display information about the first repository
print("\nSelected information about the first repository:")
print(f"Name: {first_repo['name']}")
print(f"Owner: {first_repo['owner']['login']}")
print(f"Stars: {first_repo['stargazers_count']}")
print(f"Repository: {first_repo['html_url']}")
print(f"Created: {first_repo['created_at']}")
print(f"Updated: {first_repo['updated_at']}")
print(f"Description: {first_repo['description']}")