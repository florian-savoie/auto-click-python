from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from bs4 import BeautifulSoup

# Create an instance of the webdriver class
driver = webdriver.Firefox()

# Open the login website
driver.get("http://www.buildandfight.com/")

# Find the username and password fields
username = driver.find_element(by=By.ID, value="us_log")
password = driver.find_element(by=By.NAME, value="user_pass")

# Enter your login information
username.send_keys("Crypto-flux")
password.send_keys("bfbf")

# Submit the login form
driver.find_element(by=By.XPATH, value="//input[@type='image']").click()

wait = WebDriverWait(driver, 10)
inscription_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a/img[@alt='Commerce']")))
inscription_link.click()

sleep(3)

# Click the "Berium" link
driver.execute_script("sndReqMarche('berium');")

sleep(3)

# Extract the data from the HTML table
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
rows = soup.find_all('tr')[2:] # Skip the first two rows (headers)

# Loop through each row and buy the lot
for row in rows:
    columns = row.find_all('td')
    button = columns[0].find('input')
    onclick = None
    if button and button.name == 'input' and button.get('onclick'):
        onclick = button.get('onclick')
    if onclick:
        marcheid = onclick.split("'")[1]
        driver.execute_script(f"document.getElementById('marcheid').value='{marcheid}'; var tmp=''; sndReqMarche('berium',marcheid.value,'1');")
        sleep(3)

# Close the browser
driver.quit()