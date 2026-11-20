# Scraping Laptop Specs

Scrapes the name, price and rating of laptops from a Flipkart listing page
and saves them to `products.csv`.

## How it works

1. Selenium opens the listing page in Chrome so that JavaScript-rendered
   content is loaded.
2. BeautifulSoup parses the page and finds each product card by its CSS class.
3. pandas writes the collected rows to a CSV file.

## Setup

```bash
pip install selenium beautifulsoup4 pandas
```

You also need Google Chrome installed. Selenium 4.6+ downloads a matching
chromedriver automatically.

## Run

```bash
python scrape_laptops.py
```

## Notes

- Flipkart changes its CSS class names periodically. If no products are found,
  right-click a product on the page, choose **Inspect**, and update the class
  constants at the top of `scrape_laptops.py`.
- Products with a missing field (for example, no rating yet) are kept with an
  empty value instead of crashing the script.
- Check the site's terms of service before scraping, and keep request volume low.
