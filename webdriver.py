from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (optional)

# Path to the ChromeDriver executable
chrome_driver_path = '/data/data/com.termux/files/usr/bin/chromedriver'

# Initialize the WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open a website
driver.get("https://www.youtube.com")

# Optionally, you can interact with the website
# For example, print the title of the page
print(driver.title)

# Close the browser
driver.quit()
