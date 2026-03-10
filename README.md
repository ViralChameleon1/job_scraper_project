# Automated Job Scraper + Data Cleaner
A simple Python data pipeline that scrapes webpage content, structures the data using pandas, and exports it to a CSV file.

## Project Overview
This project demonstrates a simple data pipeline built with Python.

The script performs the following steps:

1. Sends a request to a webpage
2. Parses the HTML using BeautifulSoup
3. Extracts specific elements from the page
4. Stores the extracted data in a list
5. Converts the data into a pandas DataFrame
6. Exports the cleaned data to a CSV file

This project is designed as a first attempt at web scraping and basic data processing.

## Tools Used
- Python
- requests
- BeautifulSoup (bs4)
- pandas
- SQLite / CSV storage

## How to Run
1. Clone the repository: 
    git clone https://github.com/ViralChameleon1/job_scraper_project.git
2. Navigate into the project folder:
    cd job_scraper_project
3. Install dependencies:
    pip install -r requirements.txt
4. Run the scraper:
    python scraper.py

The script will scrape webpage content and export the cleaned data to:
scraped_data.csv
