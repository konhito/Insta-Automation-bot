from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

Username1 = input("Username: ")
password1 = input("Password: ")


s = Service("C:/Users/Aditya/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.instagram.com/")
time.sleep(3)

username = driver.find_element_by_xpath(
    """/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input"""
)
# Username key
username.send_keys(Username1)
password = driver.find_element_by_xpath(
    """/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input"""
)
# passwordKey
password.send_keys(password1)

password.send_keys(Keys.ENTER)
time.sleep(6)

# users wwho you want to follow
userFollow = ["aman_danate1", "chodary6523", "dhruvsai60", "amarsahu1844"]

# loop
for i in range(len(userFollow)):
    # click on search button
    driver.find_element_by_xpath(
        """/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]"""
    ).click()

    search = driver.find_element_by_xpath(
        """/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input"""
    )
    time.sleep(3)

    search.send_keys(userFollow[i])

    time.sleep(3)

    username_click = driver.find_element_by_xpath(
        """/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]"""
    ).click()

    time.sleep(3)

    # Follow button
    username_follow = driver.find_element_by_xpath(
        """/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div"""
    ).click()

    time.sleep(3)
