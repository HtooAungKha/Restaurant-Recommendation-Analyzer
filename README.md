# Restaurant-Recommendation-Analyzer

## Authors

- Khushi Bakshi

## Project Description

The Restaurant Rating and Recommendation Analyzer is a web-based Python application that allows users to search for restaurants by city and cuisine. The application will use the Yelp Fusion API to retrieve restaurant information from the internet. Users will be able to view details such as restaurant names, ratings, prices, review counts, cuisine categories, and addresses. The collected restaurant data will be organized and stored in a local SQLite database for later analysis. The program will also generate charts and visualizations to help users compare restaurants and better understand restaurant trends in a selected location.

## Project Outline and Plan

1. Set up the GitHub repository and organize the project files.
2. Create a Flask web application with multiple pages.
3. Connect the program to the Yelp Fusion API.
4. Allow users to search for restaurants by city.
5. Allow users to filter restaurants by cuisine.
6. Retrieve restaurant information such as ratings, prices, review counts, and addresses.
7. Clean and organize the restaurant data.
8. Store the restaurant information in a local SQLite database.
9. Use Pandas to analyze the stored restaurant data.
10. Create charts using Matplotlib and Seaborn.
11. Display restaurant results and visualizations through the Flask interface.
12. Test the application and fix any errors.
13. Add installation and usage instructions to the repository.

## Interface Plan

The project will use a simple web interface built with Flask, HTML, and CSS. The home page will include a search form where users can enter a city and cuisine type. After submitting the search, users will be taken to a results page that displays restaurant names, ratings, price levels, review counts, cuisine categories, and addresses. The application will also include a statistics page where users can view charts and summaries created from the stored restaurant data. Navigation links will allow users to move between the search page, results page, and statistics page.

## Data Collection and Storage Plan

Restaurant data will be collected from the Yelp Fusion API using Python and the Requests library. The user will enter a city and cuisine type, which will be used as search parameters in the API request. The program will retrieve information such as the restaurant name, Yelp business ID, rating, price level, review count, cuisine category, address, and Yelp URL. The collected data will be cleaned and converted into a consistent format before being stored. A local SQLite database will be used to save the restaurant search results so that the data can be accessed and analyzed later. The Yelp business ID will be used as a unique identifier to help prevent duplicate restaurant records. The Yelp API key will be stored in an environment variable and will not be uploaded to GitHub.



## Data Analysis and Visualization Plan

The restaurant data stored in the SQLite database will be loaded into Pandas DataFrames for analysis. The analysis will compare restaurant ratings, cuisine categories, price levels, and review counts. Pandas will be used to calculate values such as average ratings by cuisine, the number of restaurants in each price category, and the restaurants with the highest number of reviews. Matplotlib and Seaborn will be used to create visualizations that make the results easier to understand. The planned visualizations include a bar chart showing average ratings by cuisine, a bar chart showing the distribution of restaurant price levels, and a horizontal bar chart showing the top ten restaurants by review count. The analysis results and charts will be displayed on the statistics page of the Flask application.

## Responsibilities

### Htoo Aung Kha

- Connect the application to the Yelp Fusion API
- Retrieve restaurant data
- Store restaurant data in the SQLite database
- Build the restaurant search page
- Help test the API and database functionality
- Analyze the stored restaurant data using Pandas
- Create visualizations using Matplotlib and Seaborn
- Build the statistics page
- Summarize the analysis results
- Help test the interface and visualizations


## Main Features

- Search for restaurants by city
- Filter restaurants by cuisine
- View restaurant ratings
- View restaurant price levels
- View restaurant review counts
- View restaurant addresses
- Save restaurant information to a local database
- Analyze restaurant ratings and review counts
- Display charts and graphs
- Use a simple web interface with multiple pages

## Expected Visualizations

- Average rating by cuisine shown as a bar chart
- Distribution of restaurant price levels shown as a bar chart
- Top 10 restaurants by review count shown as a horizontal bar chart

## Technologies

- Python
- Flask
- Yelp Fusion API
- SQLite
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Requests
- HTML
- CSS

## Planned Project Structure

```text
restaurant-rating-analyzer/
│
├── app.py
├── database.py
├── analysis.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── results.html
│   └── statistics.html
│
├── static/
│   └── style.css
│
└── data/
    └── restaurants.db

```
## Installation

1. Clone this repository.

```bash
git clone https://github.com/HtooAungKha/Restaurant-Recommendation-Analyzer.git
```

2. Clone this repository.

```bash
cd Restaurant-Recommendation-Analyzer
```

3. Create a virtual environment (optional but recommended).

```bash
python3 -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

4. Install the required packages.

```bash
pip3 install -r requirements.txt
```

5. Create a `.env` file in the project folder and add your Yelp API key.

```text
YELP_API_KEY=your_api_key_here
```

---

## How to Use

1. Start the Flask application.

```bash
python3 app.py
```

2. Open your web browser and go to:

```
http://127.0.0.1:5000
```

3. Enter a city and choose a cuisine.

4. Click **Search** to retrieve restaurant information from the Yelp Fusion API.

5. View restaurant details including:
   - Name
   - Rating
   - Price
   - Review count
   - Cuisine
   - Address

6. Save the search results to the SQLite database.

7. Visit the **Statistics** page to view charts and summaries based on the stored restaurant data.

---

## Future Improvements

- Add more search filters such as price range, rating, and "Open Now."
- Display restaurant locations on an interactive map.
- Allow users to save favorite restaurants.
- Export restaurant data to a CSV file.
- Add user accounts and search history.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.