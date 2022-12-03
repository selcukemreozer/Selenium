# not only any people but also any code can't beat me at https://checkboxrace.com/ !!!

from selenium import webdriver
from time import sleep
browser = webdriver.Chrome()
url = "https://checkboxrace.com/"

browser.get(url)
sleep(2)
for each in range(100):
    sleep(0.02)
    browser.find_element("xpath", "/html/body/div[1]/input["+str(each+1)+"]").click()

#for i in range(10):
#    try:
#        browser.find_element_by_xpath()

