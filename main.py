from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get('https://find-and-update.company-information.service.gov.uk/')

try:
    search_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="site-search-text"]'))
    )
    search_box.send_keys('Honch Data Limited')
    
    search_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="search-submit"]'))
    )
    search_button.click()
    
    time.sleep(10)  
    
except:
    search_box = None
result = driver.find_element(By.XPATH, '//*[@id="results"]/li[1]/h3/a')
result.click()

try:
    name = driver.find_element(By.XPATH, '//*[@id="content-container"]/div[1]/h1').text
except:
    name = None
try:
    C_number = driver.find_element(By.XPATH, '//*[@id="company-number"]/strong').text
except:
    C_number = None
try:
    c_address = driver.find_element(By.XPATH, '//*[@id="content-container"]/div[2]/div/dl/dd').text
except:
    c_address  = None

print(name, C_number, c_address)

driver.quit()
