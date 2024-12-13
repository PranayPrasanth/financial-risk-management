from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the driver (this assumes Chrome)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL of Experian on Yahoo Finance
url = 'https://finance.yahoo.com/quote/EXPN.L/key-statistics'

# Open the webpage
driver.get(url)

# Wait for the page to load fully (adjust the time if needed)
driver.implicitly_wait(10)

# Locate the "Shares Outstanding" value using XPath or CSS selector
shares_outstanding_element = driver.find_element(By.XPATH, "//td[contains(text(), 'Shares Outstanding')]/following-sibling::td")

# Get the text value of the shares outstanding
shares_outstanding = shares_outstanding_element.text

# Print the result
print(f"Shares Outstanding: {shares_outstanding}")

# Close the browser
driver.quit()
