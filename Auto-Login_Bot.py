from selenium import webdriver
import os

def startBot(username, password, url):
    path - "c:\\Users\\hp\\Downloads\\chromedriver"
    driver = webdriver.Chrome(path)
    driver.get(url)

    driver.find_element_by_name("id/class/name of username").send_keys(username)
    driver.find_element_by_name("id/class/name of password").send_keys(password)
    driver.find_element_by_css_selector("id/class/css selector of login button").click()


username = "Enter you username"
password = "Enter you password"

url = "Enter the url of login page of website"

startBot(username, password, url)


