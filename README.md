# Restaurant-Recommendation-Analyzer

## Author

- Htoo Aung Kha

## Project Description

The Restaurant Rating and Recommendation Analyzer is a Python web application that helps users search for restaurants using the Yelp Fusion API. Users can search by location and keywords to find restaurants and view information such as ratings, prices, review counts, categories, and addresses. The application retrieves restaurant data from the Yelp API and stores it in a local SQLite database. The stored data will be analyzed to generate charts and visualizations that help users compare restaurants. The goal of this project is to provide a simple and useful tool for exploring restaurants and local dining options.

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

Restaurant data is collected from the Yelp Fusion API using Python and the Requests library. Users enter a location and search keywords, and the application retrieves restaurant information such as the restaurant name, Yelp business ID, rating, price level, review count, category, address, and Yelp URL. The data is converted into Restaurant objects before being stored in a local SQLite database. The Yelp business ID is used as the primary key to prevent duplicate records. The API key is stored in a `.env` file and is not uploaded to GitHub.



## Data Analysis and Visualization Plan

The restaurant data stored in the SQLite database will be loaded into Pandas DataFrames for analysis. The analysis will compare restaurant ratings, cuisine categories, price levels, and review counts. Pandas will be used to calculate values such as average ratings by cuisine, the number of restaurants in each price category, and the restaurants with the highest number of reviews. Matplotlib and Seaborn will be used to create visualizations that make the results easier to understand. The planned visualizations include a bar chart showing average ratings by cuisine, a bar chart showing the distribution of restaurant price levels, and a horizontal bar chart showing the top ten restaurants by review count. The analysis results and charts will be displayed on the statistics page of the Flask application.


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

- Search restaurants by location
- Search restaurants using keywords
- Choose the number of search results
- View restaurant names, ratings, prices, categories, review counts, and addresses
- Automatically save restaurant information to a SQLite database
- Prevent duplicate restaurants using Yelp Business IDs
- View restaurant statistics
- Display charts for restaurant analysis
- Responsive web interface built with Flask
- Object-oriented project structure

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
- Matplotlib
- Seaborn
- Requests
- HTML
- CSS

## Planned Project Structure

```text
restaurant-recommendation-analyzer/
│
├── app.py
├── api.py
├── analysis.py
├── config.py
├── database.py
├── restaurant.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── data/
│   └── restaurants.db
│
├── static/
│   ├── style.css
│   └── charts/
│
└── templates/
    ├── base.html
    ├── index.html
    ├── results.html
    └── statistics.html
```

## Installation

1. Clone this repository.

```bash
git clone https://github.com/HtooAungKha/Restaurant-Recommendation-Analyzer.git
```

2. Go to the project folder.

```bash
cd Restaurant-Recommendation-Analyzer
```

3. Create a virtual environment.

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

1. Run the application.

```bash
python app.py
```

2. Open your browser and visit:

```
http://127.0.0.1:5000
```

3. Enter a location.

4. Enter search keywords (for example: ramen, coffee, sushi, or pizza).

5. Enter the number of restaurants to display (or press Enter to use the default value of 30).

6. Click **Search**.

7. Browse the restaurant results.

8. Visit the **Statistics** page to view charts and restaurant analysis.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Screenshots

### Home Page

![Home Page](Screenshots/home-page.png)

### Search Results

![Search Results](Screenshots/search-results.png)

### Statistics Dashboard

![Statistics Dashboard](Screenshots/dashboard.png)