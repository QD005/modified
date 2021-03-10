from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import browser
brower= browser
username='spectrammedia'
password='Backsp@c5'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("window-size=1920x1480")
chrome_options.add_argument("disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(
chrome_options=chrome_options, executable_path=ChromeDriverManager().install()
)


#chrome_options = webdriver.ChromeOptions()
#######chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--disable-dev-shm-usage")
#chrome_options.add_argument("--no-sandbox")
#driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
driver.implicitly_wait(60)

driver.get("https://www.instagram.com/")
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "svg[aria-label='Home']")))
print("###################################")
print("It is logged")
print("###################################")

instaAccounts = os.environ.get("peopleList").split(" ")

for account in instaAccounts:
    print("https://www.instagram.com/{}".format(account))
    driver.get("https://www.instagram.com/{}".format(account))
    driver.find_element(By.CSS_SELECTOR, "article a").click()
    try:
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "svg[aria-label='Unlike']")))
        print("###################################")
        print("The post is already liked")
        print("###################################")
    except:
        driver.find_element(By.CSS_SELECTOR, "svg[aria-label='Like']").click()
        print("###################################")
        print("The post was liked")
        print("###################################")

driver.quit()