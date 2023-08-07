from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import random


s = Service("C:/Users/Aditya/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.instagram.com/")
sleep_time = random.uniform(3, 6)

time.sleep(sleep_time)

username = driver.find_element_by_xpath(
    """/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input"""
)
username.send_keys("aman_danate")
password = driver.find_element_by_xpath(
    """/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input"""
)
password.send_keys("fakeid")

password.send_keys(Keys.ENTER)
sleep_time1 = random.uniform(3, 6)
time.sleep(sleep_time1)


userFollow = ["aman_danate1", "chodary6523", "dhruvsai60", "amarsahu1844"]


for i in range(len(userFollow)):
    driver.get(f"https://www.instagram.com/{userFollow[i]}")

    sleep_time2 = random.uniform(3, 6)

    time.sleep(sleep_time2)

    username_follo = driver.find_element_by_xpath(
        """/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div"""
    ).click()
    sleep_time3 = random.uniform(3, 6)

    time.sleep(sleep_time3)
