import requests
from bs4 import BeautifulSoup

url = "https://christsquare.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)  # Extracts the page title

# pip install beautifulsoup4