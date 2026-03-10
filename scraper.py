import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

def fetch_page(url):
    """Fetch webpage HTML."""
    response = requests.get(url, verify=False)
    response.raise_for_status()
    return response.text

def parse_jobs(soup):
    job_cards = soup.find_all("div", class_="card-content")
    job_data = []
    for job in job_cards:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        job_data.append({
            "title": title,
            "company": company,
            "location": location
        })
    return job_cards, job_data

def save_results(df):
    df.to_csv("scraped_data.csv", index=False)
    print("Data saved to scraped_data.csv")

    conn = sqlite3.connect("jobs.db")
    df.to_sql("jobs", conn, if_exists="replace", index=False)
    conn.close()

def main():

    # Start pipeline
    print("Starting job scraping pipeline...")

    # Target job listings page
    url = "https://realpython.github.io/fake-jobs/"

    # Fetch webpage
    html = fetch_page(url)

    # --- Debugging checks used during development ---
    # print(response.status_code)
    # print(response.text[:500])
    # --- End debugging checks ---

    # Parse HTML
    soup = BeautifulSoup(html, "html.parser")

    # Locate job listing cards
    job_cards, job_data = parse_jobs(soup)
    print(f"{len(job_cards)} jobs found")

    # Build DataFrame
    df = pd.DataFrame(job_data)

    save_results(df)

    # Finish pipeline
    print("Pipeline completed successfully.")


# Run script
if __name__ == "__main__":
    main()