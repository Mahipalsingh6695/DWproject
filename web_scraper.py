import requests
from bs4 import BeautifulSoup
import json

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract text from all content without HTML tags
    data = []
    for section in soup.find_all(['h1', 'h2', 'p']):  # Adjust tags as needed
        cleaned_text = section.get_text(strip=True)  # Removes HTML tags
        if cleaned_text:  # Avoid storing empty strings
            data.append({"text": cleaned_text})

    return data

def save_to_json(data, file_name="website_data.json"):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    website_url = "https://kpimining.com/"  # Replace with the target website URL
    scraped_data = scrape_website(website_url)
    save_to_json(scraped_data)
    print(f"Data saved to website_data.json")
