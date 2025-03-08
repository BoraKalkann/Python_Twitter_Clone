

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

number = "Your Number"
password = "Your Password"

class twitterBot:
    def __init__(self,number,password):
        self.browserProfile= webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("prefs",{"intl.accept_languages":"en,en_US"})
        self.browser = webdriver.Chrome("chromedriver.exe",chrome_options=self.browserProfile)
        self.number = number
        self.password = password
    def signIn(self):
        self.browser.get("https://x.com/i/flow/login")
        time.sleep(2)
        self.browser.find_element(By.XPATH,"/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div/div[4]/label/div/div[2]/div/input")

twitter = twitterBot(number,password)
twitter.signIn()
