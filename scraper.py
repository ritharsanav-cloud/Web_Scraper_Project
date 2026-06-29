import requests
from bs4 import BeautifulSoup
import csv

all_quotes = []

for page in range(1, 11):

    url = f"https://quotes.toscrape.com/page/{page}/"

    response = requests.get(url)

    if response.status_code == 200:

        print(f"Page {page} scraped successfully")

        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("span", class_="text")
        authors = soup.find_all("small", class_="author")

        for quote, author in zip(quotes, authors):
            all_quotes.append([quote.text, author.text])

    else:
        print(f"Failed to scrape page {page}")

with open("quotes.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(["Quote", "Author"])

    writer.writerows(all_quotes)

print("\nData saved to quotes.csv")
print("Total Quotes Found:", len(all_quotes))

author_name = input("\nEnter author name to search: ")

found = False

for quote, author in all_quotes:
    if author_name.lower() in author.lower():
        print("\nAuthor:", author)
        print("Quote :", quote)
        print("-" * 50)
        found = True

if not found:
    print("No quotes found for that author.")