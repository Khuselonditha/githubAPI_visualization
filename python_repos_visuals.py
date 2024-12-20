# imports
import requests
import plotly.express as px
from plotly import offline

# Make an API call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>1000"

headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers)
print(f"Status code: {response.status_code}")

# Process the results
response_dict = response.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Process repository information
repo_dict = response_dict["items"]
repo_names, stars = [], []      # Lists to store repository names and stars
for repo in repo_dict:
    repo_names.append(repo["name"])
    stars.append(repo["stargazers_count"])

# Make visualization
fig = px.bar(x=repo_names, y=stars, title="Most-Starred Python Projects on GitHub")
fig.update_layout(xaxis_title="Repositories", yaxis_title="Stars")
offline.plot(fig, filename='charts/most_starred_python_repos.html')
