import time
from selenium.webdriver.common.by import Byfrom selenium import webdriverfrom selenium.webdriver.common.keys import Keysdriver = webdriver.Chrome(executable_path="C:/Users/win10/Desktop/auto/chromedriver_win32/chromedriver.exe")driver.get("https://teams.microsoft.com/_#/school/teams-grid/General?ctx=teamsGrid")time.sleep(2)element = driver.find_element_by_name("loginfmt")if element.is_displayed():    element.send_keys("ankush.choudhary2021@vitstudent.ac.in")    button = driver.find_element_by_xpath(        "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input")    button.click()    element = driver.find_element_by_name("passwd")    element.send_keys("r44hT#6S")    time.sleep(1)    button = driver.find_element_by_xpath(        "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input")    button.click()    time.sleep(1)    button = driver.find_element_by_xpath(        "/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input")    button.click()    time.sleep(1)    button = driver.find_element_by_xpath(        "/html/body/ohp-app/div/div/div[1]/ohp-left-nav-react/ohp-left-nav-react-content/div/div[1]/ul/li[10]/div/a/div/i")    button.click()    time.sleep(1)