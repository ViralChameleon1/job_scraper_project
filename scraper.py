#Run Start message
print("Starting job scraping pipeline...")

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the webpage we want to scrape
url = "https://example.com"

# Send a request to the website
# verify=False temporarily bypasses SSL issues
response = requests.get(url, verify=False)

# Confirm the request worked
# 200 = success
print(response.status_code)

# Print the first 500 characters
# of the page HTML so we can inspect it
    #print(response.text[:500])


# Parse the HTML using BeautifulSoup
# converts raw HTML into a structure that I can search and extract data from
soup = BeautifulSoup(response.text, "html.parser")

# Extract and print the page title
title = soup.title.text
print(title)

# Extract and print the main heading from the page
heading = soup.find("h1").text
print(heading)

# Extract and print the first paragraph from the page
paragraph = soup.find("p").text
print(paragraph)

# Extract all paragraph elements from the page and store their data in a list
paragraphs = soup.find_all("p")
paragraph_list = []
for p in paragraphs:
    text = p.text
    print(text)
    paragraph_list.append(text)
    
# Convert scraped data into a pandas DataFrame and print it
df = pd.DataFrame(paragraph_list, columns=["paragraph_text"])
print(df)

# Save the DataFrame to a CSV file
df.to_csv("scraped_data.csv", index=False)
print("Data saved to scraped_data.csv")

#Run finished messaage
print("Pipeline completed successfully.")