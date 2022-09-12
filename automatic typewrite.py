#auto typer 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://typing-speed-test.aoeu.eu/"
driver = webdriver.Firefox()
driver.get(url)

driver.implicitly_wait(0.5)  # make the cookie load

AGREE = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/button[2]') #accept the cookie
AGREE.click()

total_words = driver.find_elements(By.CLASS_NAME,"currentword") + driver.find_elements(By.CLASS_NAME,"nextword")

input_area = driver.find_element(By.ID, "input")
input_area.click()
for word in total_words: #read current word
    #put the input
    input_area.send_keys(word.text)
    input_area.send_keys(Keys.SPACE)

