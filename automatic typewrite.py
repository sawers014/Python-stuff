from ctypes import alignment
import tkinter as tk
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

root= tk.Tk()
canvas1 = tk.Canvas(root, width = 500, height = 400, bg='black')
canvas1.pack()

def type(driver): #typewrite
    url = "https://typing-speed-test.aoeu.eu/"
    
    
    driver.get(url) #open the url

    driver.implicitly_wait(0.5)  # make the cookie load
    try:
        AGREE = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/button[2]') 
        AGREE.click() #accept the cookie
    except:
        driver.implicitly_wait(0.01)

    total_words = driver.find_elements(By.CLASS_NAME,"currentword") + driver.find_elements(By.CLASS_NAME,"nextword")
    input_area = driver.find_element(By.ID, "input")
    
    driver.execute_script("arguments[0].scrollIntoView();", input_area)
    input_area.click()
    for word in total_words: #read current word
        input_area.send_keys(word.text + " ") #put the input
def fire ():  #button "firefox", it will start the program with firefox
    label1 = tk.Label(root, text= 'opening program with firefox', fg='blue', font=('helvetica', 12, 'bold'))
    canvas1.create_window(250, 200, window=label1)
    type(webdriver.Firefox())
def chr ():  #button "chrome", it will start the program with chrome

    label1 = tk.Label(root, text= 'opening program with chrome', fg='red', font=('helvetica', 12, 'bold'))
    canvas1.create_window(250, 200, window=label1)
    type(webdriver.Chrome())

label3 = tk.Label(root, text= 'Chose a Browser to use for the typewriter', fg='blue',bg='gray', font=('timesnewroman', 19, 'bold'))   # "chose a browser... text
canvas1.create_window(250, 100, window=label3)

button1 = tk.Button(text='Firefox', command=fire, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

button2 = tk.Button(text='Chrome', command=chr, bg='yellow',fg='black')
canvas1.create_window(350, 150, window=button2)



root.mainloop()
