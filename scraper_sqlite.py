# scraper.py
import requests
from bs4 import BeautifulSoup
import sqlite3

# SQLite Database Setup
def create_database():
    conn = sqlite3.connect('chatbot.db')  # Create SQLite DB if not exists
    cursor = conn.cursor()
    
    # Create table for storing website content
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to scrape website and store data in SQLite
def scrape_website_to_sqlite(url='https://kpimining.com'):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch the website. HTTP Status: {response.status_code}")
            return

        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')

        conn = sqlite3.connect('chatbot.db')
        cursor = conn.cursor()

        for p in paragraphs:
            content = p.get_text().strip()
            if content:
                cursor.execute('INSERT INTO data (content) VALUES (?)', (content,))
        
        conn.commit()
        conn.close()
        print("Website content scraped and stored in SQLite database!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_database()  # Create SQLite database (run this once)
    scrape_website_to_sqlite('https://kpimining.com')  # Replace with your target URL
