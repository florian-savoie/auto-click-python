from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Créez une instance de la classe webdriver
driver = webdriver.Firefox()

# Ouvrez le site web de connexion
driver.get("http://www.buildandfight.com/")

# Trouvez les champs de nom d'utilisateur et de mot de passe
username = driver.find_element(by=By.ID, value="us_log")
password = driver.find_element(by=By.NAME, value="user_pass")

# Entrez vos informations de connexion
username.send_keys("Crypto-flux")
password.send_keys("bfbf")


# Soumettez le formulaire de connexion
driver.find_element(by=By.XPATH, value="//input[@type='image']").click()

wait = WebDriverWait(driver, 10)
inscription_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a/img[@alt='Commerce']")))
inscription_link.click()

sleep(3)

# Cliquez sur le lien "Berium"
driver.execute_script("sndReqMarche('berium');")

sleep(3)


buy_buttons = driver.find_elements(By.XPATH, "//input[starts-with(@id, 'input_') and @value='acheter']")
print("Nombre de lots disponibles : ", len(buy_buttons))
sleep(3)




for i in range(len(buy_buttons)):
    driver.execute_script("sndReqMarche('berium');")
    sleep(1)
    buy_buttons = driver.find_elements(By.XPATH, "//input[starts-with(@id, 'input_') and @value='acheter']")
for button in buy_buttons:
    sleep(1)
    button.click()
    sleep(1)
