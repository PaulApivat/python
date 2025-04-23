import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Path to your ChromeDriver
CHROME_DRIVER_PATH = "/path/to/chromedriver"

# Configure Chrome options (you can add more options if needed)
chrome_options = Options()
chrome_options.add_argument(
    "--headless"
)  # Run in headless mode if you don't want to open the browser window
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

# Initialize Chrome WebDriver
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Go to the Twitter list URL
url = "https://x.com/i/lists/1749843181544333341/members"
driver.get(url)


# Exponential backoff function
def exponential_backoff(attempt, base_time=2, cap=60):
    # Calculate the wait time as base_time ^ attempt, with a maximum of 'cap' seconds
    wait_time = min(base_time**attempt, cap)
    # Add some randomness to avoid being too predictable
    wait_time += random.uniform(0, 1)
    print(f"Sleeping for {wait_time:.2f} seconds...")
    time.sleep(wait_time)


# Initialize backoff attempt counter
attempt = 1

# Allow time for the dynamic content to load initially
time.sleep(5)

# Scroll down the page to load more members, using exponential backoff
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    try:
        # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait with exponential backoff
        exponential_backoff(attempt)

        # Calculate new scroll height and compare with the last height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # Break if no more content is loaded
            break
        last_height = new_height

        # Reset backoff attempt after a successful scroll
        attempt = 1
    except Exception as e:
        print(f"An error occurred: {e}")
        # Increase the attempt counter and retry with exponential backoff
        exponential_backoff(attempt)
        attempt += 1
        if attempt > 5:  # After 5 failed attempts, break
            print("Max retries reached, stopping script.")
            break

# Extract the members' details after scrolling
members = driver.find_elements(By.XPATH, "//div[@dir='ltr']/span/span")

# Print the screen names or descriptions
for member in members:
    print(member.text)

# Close the driver
driver.quit()
