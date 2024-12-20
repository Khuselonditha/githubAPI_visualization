# GitHub API Visualization

This project visualizes data from the GitHub API using Python. The script `python_repos_visuals.py` fetches data about the most popular Python repositories on GitHub and generates visualizations to display this information.

## Features

- Fetches the most-starred Python projects with over 1000 stars using the GitHub API.
- Processes repository metadata, including names, stars, and descriptions.
- Visualizes the top 20 repositories in an interactive bar chart.
- Displays repository names as clickable links and provides hover text with additional information.

## Requirements

- Python 3.x
- `requests` library
- `plotly.express` library

## Installation

1. Clone the repository:
    ```bash
    git clone git@github.com:Khuselonditha/githubAPI_visualization.git
    ```
2. Navigate to the project directory:
    ```bash
    cd githubAPI_visualization
    ```
3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## How to run

1. Clone this repository or copy the script to your local machine.
2. Run the script:
```bash
python python_repos_visuals.py
```
3. The script will create an interactive HTML file in the charts directory:
    -  most_starred_python_repos.html
4. Open the file in your browser to view the chart.


## Key Components

1. **API Call**:
    - Uses the GitHub API to fetch Python repositories with more than 1000 stars.
    - Sends a request with appropriate headers to ensure compatibility.

2. **Data Processing**:
    - Extracts repository names, star counts, and descriptions.
    - Formats repository names as clickable links.
3. **Visualization**:
    - Creates a bar chart using Plotly Express.
    - Customizes chart appearance with color and interactivity.


## Example Output
An interactive bar chart with:
- Repository names on the x-axis (as clickable links).
- Star counts on the y-axis.
- Hover text showing repository owner and description.  


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [GitHub API](https://docs.github.com/en/rest)
- [Plotly](https://plotly.com/python/)
