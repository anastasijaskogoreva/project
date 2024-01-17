import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
option = webdriver.ChromeOptions()   # internet brauzeris
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.ss.lv/lv/transport/cars/"  # saite
driver.get(url)
time.sleep(2)

find=driver.find_element(By.ID, "ahc_166")     # mašīnas marka
find.click()

find=driver.find_element(By.CLASS_NAME, "a19")  # jauni sludinajumi
find.click()
time.sleep(1)

find=driver.find_element(By.ID,"f_o_8_min")  # min cena
find.send_keys("1000")  # kāda min cena
find=driver.find_element(By.ID,"f_o_8_max")  # max cena
find.send_keys("9000")  # kāda max cena
time.sleep(1)

find=driver.find_element(By.CLASS_NAME, "b.s12") # meklēt 
find.click()
time.sleep(1)

input()
