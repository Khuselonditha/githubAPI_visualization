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
repo_links, stars, hover_texts = [], [], []    # Lists to store repository names and stars

# Extract info form first 20 repos for visualization
for repo in repo_dict[0:20]:
    # Turn repo names into links
    repo_name = repo["name"]
    repo_url = repo["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo["stargazers_count"])

    # Build hover text
    owner = repo["owner"]["login"]
    description = repo["description"]
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Make visualization
title = "Most-Starred Python Projects on GitHub"
labels = {"x": "Repository", "y": "Stars"}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels,
            hover_name=hover_texts)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, 
                yaxis_title_font_size=20)

# Customize colour makers
fig.update_traces(marker_color="SteelBlue", marker_opacity=0.6)


offline.plot(fig, filename='charts/most_starred_python_repos.html')