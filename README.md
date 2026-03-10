# Automated Job Scraper + Data Cleaner
A simple Python data pipeline that scrapes job listings from a webpage, structures the data using pandas, and stores the results in a SQLite database.

## Project Overview
This project demonstrates a simple data pipeline built with Python.

The script performs the following steps:

1. Sends a request to a webpage containing job listings
2. Parses the HTML using BeautifulSoup
3. Extracts structured job data (title, company, location)
4. Stores the extracted records in a list
5. Converts the data into a pandas DataFrame
6. Saves the processed data to both a CSV file and a SQLite database

The pipeline is organized into modular functions:

- `fetch_page()` – retrieves the webpage HTML
- `parse_jobs()` – extracts job information from the page
- `save_results()` – stores the processed data
- `main()` – orchestrates the pipeline

This project is designed as a first attempt at web scraping and basic data processing.

## Tools Used
- Python
- requests
- BeautifulSoup (bs4)
- pandas
- SQLite

## How to Run
1. Clone the repository:  
    git clone https://github.com/ViralChameleon1/job_scraper_project.git  

2. Navigate into the project folder:  
    cd job_scraper_project  

3. Install dependencies:  
    pip install -r requirements.txt  

4. Run the scraper:  
    python scraper.py  

The script will scrape job listings and store the processed data in:
scraped_data.csv  
jobs.db