from selenium.webdriver.common.by import By
from BaseApp import BasePage


class SeacrhLocators:
    LOCATOR_SEARCH_CONTACT = (By.CLASS_NAME, "sbisru-Header__menu-item-1")
    LOCATOR_SEARCH_TENSOR_LOGO = (By.CLASS_NAME, "sbisru-Contacts__logo-tensor")
    LOCATOR_SEARCH_POWER_IN_PEOPLE = (By.XPATH,'//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]')
    LOCATOR_SEARCH_MORE_DETAILS = (By.XPATH,'//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
    LOCATOR_SEARCH_DIV_WITH_IMG = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]')
    LOCATOR_SEARCH_ALL_IMG = By.TAG_NAME,'img'
    LOCATOR_SEARCH_REGION = (By.CLASS_NAME, 'sbis_ru-Region-Chooser__text')
    LOCATOR_SEARCH_SWITCH_REGION = (By.CLASS_NAME, 'sbisru-Contacts-List__item')
    LOCATOR_SEARCH_ALL_SPAN = (By.CLASS_NAME, 'sbis_ru-Region-Panel__list')
    LOCATOR_SEARCH_FOOTER = (By.CLASS_NAME, 'sbisru-Footer__container')
    LOCATOR_SEARCH_DOWNLOAD_SBIS = (By.TAG_NAME, 'div')
    LOCATOR_SEARCH_PLAGIN = (By.CLASS_NAME,'controls-TabButton')
    LOCATOR_SEARCH_DOWNLOAD_BLOCK = (By.CLASS_NAME, 'sbis_ru-DownloadNew-block')  

class SearchHelper(BasePage):
    def search_contacts(self):
        return self.find_element(SeacrhLocators.LOCATOR_SEARCH_CONTACT).click()
    def find_tensor_logo(self):
        return self.find_element(SeacrhLocators.LOCATOR_SEARCH_TENSOR_LOGO).click()
    def find_block_power_people(self):
         return self.find_element(SeacrhLocators.LOCATOR_SEARCH_POWER_IN_PEOPLE)
    def find_show_more_details(self):
        return self.find_element(SeacrhLocators.LOCATOR_SEARCH_MORE_DETAILS)
    def cheack_size(self):    
      about_element = self.find_element(SeacrhLocators.LOCATOR_SEARCH_DIV_WITH_IMG) # <--- Находим div со всеми img
      img_elements = about_element.find_elements(By.TAG_NAME,'img') # <--- Находим все img
      return {elem.value_of_css_property("height") for elem in img_elements} | {elem.value_of_css_property("width") for elem in img_elements}
    
    def find_main_title(self):
        return self.get_title()
    def find_main_url(self):
        return self.get_url()
    def find_region(self):
        return self.find_element(SeacrhLocators.LOCATOR_SEARCH_REGION)
    def find_partner(self):
        return self.find_elements(SeacrhLocators.LOCATOR_SEARCH_SWITCH_REGION)
    def find_span(self):
        spans = self.find_element(SeacrhLocators.LOCATOR_SEARCH_ALL_SPAN)
        return spans.find_elements(By.TAG_NAME, 'li')
    def find_download_sbis(self):
        footer = self.find_element(SeacrhLocators.LOCATOR_SEARCH_FOOTER)
        download_sbis = footer.find_elements(By.TAG_NAME, 'div')
        download_sbis_li = download_sbis[9].find_elements(By.TAG_NAME,'li')
        download_sbis_li_list = [elem for elem in download_sbis_li if(elem.text=='Скачать СБИС')]
        dwn = download_sbis_li_list[0].find_element(By.TAG_NAME, 'a')
        return dwn
    def find_download_plagin(self):
        return self.find_elements(SeacrhLocators.LOCATOR_SEARCH_PLAGIN)
    def find_download_block(self):
        d_block = self.find_elements(SeacrhLocators.LOCATOR_SEARCH_DOWNLOAD_BLOCK)
        download_text = [elem for elem in d_block if('Скачать' in elem.text)]
        find_download_link = download_text[0].find_element(By.TAG_NAME, 'a')
        return find_download_link, download_text[0]