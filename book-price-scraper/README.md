# Python Web Scraper: E-Commerce Book Data Extractor

An automated data collection tool built in Python to extract product details
from an e-commerce storefront sandbox.

It scrapes [Books to Scrape](https://books.toscrape.com/), a website designed
explicitly for practicing web scraping legally.

## Features

- Extracts product titles, pricing data and stock availability.
- Formats nested HTML data using clean text utilities.
- Automatically generates a structured `books_dataset.csv` file for
  analytical use.

## Technical Stack

- **Language:** Python 3
- **Libraries:** BeautifulSoup4 (HTML parsing), Requests (HTTP requests),
  CSV (data handling)

## Installation & Usage

1. Clone this repository to your machine.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python scraper.py
   ```

The script prints each book as it is scraped and writes the full dataset to
`books_dataset.csv`:

```text
Title,Price,Availability
A Light in the Attic,£51.77,In stock
Tipping the Velvet,£53.74,In stock
...
```

## Possible next steps

- **Pagination:** follow the "next" links to scrape all 50 pages of the
  catalogue.
- **Data cleaning:** convert the currency text (like `£51.77`) into float
  values for calculations.
- **Visualization:** plot book pricing trends with matplotlib.
