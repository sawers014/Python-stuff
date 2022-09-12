# web browser opener
#TODO count element with same class name
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

total_words = driver.find_element(By.CLASS_NAME,"nextword")
print(total_words)
for word in range(500):
    #read current word
    word = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "currentword"))
    )
    #put the input
    input_area = driver.find_element(By.ID, "input")
    input_area.click()
    input_area.send_keys(word.text)
    input_area.send_keys(Keys.SPACE)


