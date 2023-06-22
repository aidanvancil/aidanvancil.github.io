import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
url = 'https://www.example.com'
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find elements by tag name
elements = soup.find_all('tag_name')

# Find elements by class name
elements = soup.find_all(class_='class_name')

# Find elements by ID
element = soup.find(id='element_id')

# Extracting text from an element
text = element.get_text()

# Extracting attribute value
attribute_value = element['attribute_name']

# Navigating the HTML structure
parent_element = element.parent
next_sibling_element = element.next_sibling
previous_sibling_element = element.previous_sibling

# Scraping data from multiple pages
urls = ['https://www.example.com/page1', 'https://www.example.com/page2']
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Perform scraping operations on each page

# Handling errors and exceptions
try:
    example_code_here = None
except Exception as e:
    print('An error occurred:', str(e))

# Using CSS selectors
selected_elements = soup.select('css_selector')

# Extracting data from tables
table = soup.find('table')
rows = table.find_all('tr')
for row in rows:
    columns = row.find_all('td')
    for column in columns:
        print(column.get_text())

# Writing scraped data to a file
with open('output.txt', 'w') as file:
    file.write('Scraped data')

# Simulating a browser session (using cookies, headers, etc.)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get(url, headers=headers, cookies=cookies)

# Handling JavaScript-rendered websites (using tools like Selenium)
from selenium import webdriver
driver = webdriver.Chrome()
driver.get(url)
# Perform scraping operations using Selenium

# Handling authentication
# If the website requires authentication, you may need to include credentials in the request headers or use a login form.
