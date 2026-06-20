import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
response = requests.get(url)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

quotes = []

for quote in soup.find_all("span", class_="text"):
    quotes.append(quote.text)

print("Quotes Found:", len(quotes))

df = pd.DataFrame({"Quote": quotes})

df.to_csv("quotes_dataset.csv", index=False)

print("Dataset created successfully!")