import csv

import requests
from bs4 import BeautifulSoup

# The official sandbox URL for learning web scraping
URL = "https://books.toscrape.com/"


def scrape_books():
    # 1. Fetch the website HTML
    response = requests.get(URL, timeout=30)
    if response.status_code != 200:
        print(f"Failed to load page. Status: {response.status_code}")
        return

    # The site is UTF-8 but does not declare it in the HTTP headers,
    # so requests would guess wrong and garble the £ sign
    response.encoding = "utf-8"

    # 2. Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # 3. Locate all book containers on the page
    books = soup.find_all("article", class_="product_pod")

    scraped_data = []

    print(f"--- Scraping {len(books)} books from Books to Scrape ---")

    # 4. Loop through each book container to pull specific data
    for book in books:
        # Extract title from the anchor tag title attribute
        title = book.h3.a["title"]

        # Extract price string
        price = book.find("p", class_="price_color").text

        # Extract availability status
        availability = book.find("p", class_="instock availability").text.strip()

        scraped_data.append([title, price, availability])
        print(f"Saved: {title[:30]}... | {price}")

    # 5. Export everything to a clean CSV file
    with open("books_dataset.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Availability"])  # Headers
        writer.writerows(scraped_data)

    print("\nSuccess! All data exported to 'books_dataset.csv'")


if __name__ == "__main__":
    scrape_books()
