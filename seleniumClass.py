from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import os

class SeleniumInterface():
   def CreateConnection(self):
      options = webdriver.ChromeOptions() 
      options.add_experimental_option("excludeSwitches", ["enable-logging"])
      options.add_experimental_option("detach", True)
      prefs = {
         'download.default_directory' : os.getcwd(),
         "download.prompt_for_download": False,
         "download.directory_upgrade": True,
         "safebrowsing.enabled": True,
      }
      options.add_experimental_option('prefs', prefs)
      options.binary_location = f"{os.getcwd()}\\chrome-win64\\chrome.exe" 
      service = Service(executable_path=f'{os.getcwd()}/chromedriver.exe') 
      driver = webdriver.Chrome(service=service, options=options)
      return driver
   def CloseConnection(self, driver):
      return driver.quit()