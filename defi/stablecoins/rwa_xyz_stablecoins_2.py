from selenium import webdriver
from bs4 import BeautifulSoup
import time

# URL of the website
url = "https://app.rwa.xyz/stablecoins"

# Set up Selenium with Chrome Driver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Open the URL
driver.get(url)

# Wait for JavaScript to load
time.sleep(5)  # Adjust the sleep time if necessary

# Get the page source
soup = BeautifulSoup(driver.page_source, "html.parser")

# Find the div containing the table
table_div = soup.find("div", class_="mt-4")

if table_div:
    # Find the table element within the div
    table = table_div.find("table", class_="min-w-full")
    print("Found table_div")

    if table:
        # Find the tbody element with the specified class
        tbody = table.find(
            "tbody", class_="divide-y divide-brand-gray-300 bg-white transition-opacity"
        )

        if tbody:
            # Find all rows in the table body
            rows = tbody.find_all(
                "tr",
                class_="flex flex-row group/row bg-grid-row-striped divide-x divide-x-brand-gray-300",
            )

            # Loop through each row
            for row in rows:
                # Extract data from each column in the row
                columns = row.find_all("td")
                row_data = [column.get_text(strip=True) for column in columns]

                # Print the row data
                print(row_data)
        else:
            print("Tbody not found.")
    else:
        print("Table not found.")
else:
    print("Table div not found.")

# Close the driver
driver.quit()
