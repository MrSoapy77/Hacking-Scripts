"""Scrape laptop names, prices and ratings from a Flipkart listing page.

Writes the results to products.csv. See README.md for setup.
"""
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

URL = (
    "https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr"
    "?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2"
)

# Flipkart changes these CSS class names from time to time. If the script
# finds no products, inspect the page and update them.
PRODUCT_LINK_CLASS = "_31qSD5"
NAME_CLASS = "_3wU53n"
PRICE_CLASS = "_1vC4OE _2rQ-NK"
RATING_CLASS = "hGSR34 _2beYZw"


def text_or_empty(tag):
    return tag.get_text(strip=True) if tag else ""


def scrape(url=URL):
    driver = webdriver.Chrome()  # Selenium 4.6+ finds chromedriver itself
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
    finally:
        driver.quit()

    rows = []
    for link in soup.find_all("a", href=True, attrs={"class": PRODUCT_LINK_CLASS}):
        rows.append({
            "Product Name": text_or_empty(link.find("div", attrs={"class": NAME_CLASS})),
            "Price": text_or_empty(link.find("div", attrs={"class": PRICE_CLASS})),
            "Rating": text_or_empty(link.find("div", attrs={"class": RATING_CLASS})),
        })
    return rows


if __name__ == "__main__":
    products = scrape()
    pd.DataFrame(products).to_csv("products.csv", index=False, encoding="utf-8")
    print(f"Saved {len(products)} products to products.csv")
