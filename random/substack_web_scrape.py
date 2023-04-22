
import requests
from bs4 import BeautifulSoup

# URL of the substack.com page to scrape
url = 'https://cryptorisks.substack.com/p/asset-risk-assessment-defi-franc'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the article titles on the page
post_title = soup.find_all('h1', {'class': 'post-title unpublished'})
subtitle = soup.find('h3', {'class': 'subtitle'})
body = soup.find('div', {'class': 'body markup'})

# Print the titles to the console
for title in post_title:
    print(title.text)

print(subtitle.text)
print(body.text)