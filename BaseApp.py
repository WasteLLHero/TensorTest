from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://sbis.ru/'

    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")
    def go_to_site(self):
        return self.driver.get(self.url)
    
    def switch_to_window(self, new_window):
        return self.driver.switch_to.window(new_window)
    def get_title(self):
        return self.driver.title
    def get_url(self):
        return self.driver.current_url
    def close_window(self):
        return self.driver.close()
    
