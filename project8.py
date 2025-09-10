import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

for i, item in enumerate(soup.select(".storylink")[:5], 1):
    print(f"{i}. {item.text}")
