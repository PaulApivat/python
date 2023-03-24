import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Set up the Chrome driver with headless options
options = Options()
options.add_argument('--headless')
service = Service('/path/to/chromedriver') # replace with the path to your chromedriver executable
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the website
url = 'https://de.fi/rekt-database'
driver.get(url)

# Check if the page contains the "You need to enable JavaScript" message
if "<noscript>You need to enable JavaScript to run this app.</noscript>" in driver.page_source:
    # If so, run JavaScript to get around it
    driver.execute_script("document.querySelector('noscript').remove();")

# Get the updated page source
html = driver.page_source

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the body tag
# body = soup.find('body')
section = soup.find('section')

# Find all nested divs with class 'scam-database-table'
#scam_tables = section.find_all('div', class_='scam-database-table')
scam_tables = section.find_all('div', class_='scam-database-body')

# Find all nested div tags within the 'scam-database-body' div
#rows = scam_tables.find('div', class_='row')

# Extract the data from each row

data = {}

for row in scam_tables:
    chain = row.find('span', class_='content').text
    funds_lost = row.find_all('span', class_='content orange')[0].text
    issue = row.find_all('span', class_='content')[-2].text
    date = row.find_all('span', class_='content')[-1].text
    print(f"Chain: {chain}, Funds lost: {funds_lost}, Issue: {issue}, Date: {date}")

# Quit the driver


driver.quit()