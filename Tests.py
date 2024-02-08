from pages import SearchHelper
import re, os, glob
import time
def test_first(browser):
   main_page = SearchHelper(browser)
   main_page.go_to_site()
   main_page.search_contacts()
   main_page.find_tensor_logo()
   
   main_page.switch_to_window(browser.window_handles[-1])
   text_power_people = main_page.find_block_power_people()
   assert text_power_people.text=='Сила в людях', 'The "Strength in people" block is missing' # <--- Проверяем есть ли блок "Сила в людях" (используя заголовок)
   element_power_people = main_page.find_show_more_details()
   browser.execute_script("arguments[0].click();", element_power_people) # <-- Переходим в "Подробнее"
   main_page.switch_to_window(browser.window_handles[-1])
   assert browser.current_url=='https://tensor.ru/about', 'Different Url' # <--- Убеждаемся, что открылся нужный url
   check_img_size = main_page.cheack_size() 
   assert len(check_img_size) == 2, 'Different image size' # <--- Проверям кол-во элементов, если len = 2, то все фотографии одинаковые
    

def test_second(browser):
   main_page = SearchHelper(browser)
   main_page.go_to_site()
   main_page.search_contacts()
   home_region_title = main_page.find_main_title()
   home_region_url = main_page.find_main_url()
   region = main_page.find_region()
   assert region.text == 'Тюменская обл.', "Different region"  # <--- Проверяем регион, в моем случае Тюмень
   print(f"Region text --->>> {region.text}")
   partner_list = main_page.find_partner()
   print([item.text for item in partner_list])
   region.click()
   spans = main_page.find_span()
   span_li_list = [elem for elem in spans if(elem.text == '41 Камчатский край')] # <-- Сохраняем нужный нам li
   span_li_list[0].click()
   time.sleep(2)
   print(f"Home title ---> {home_region_title}, current title ---> {main_page.get_title()} \nHome url ---> {home_region_url}, current url ---> {main_page.get_url()}")
   assert main_page.get_title() != home_region_title, 'Not different title'
   assert main_page.get_url() != home_region_url, 'Not different url'
   
def test_third(browser):
   main_page = SearchHelper(browser) 
   main_page.go_to_site() 
   download_sbis = main_page.find_download_sbis()
   browser.execute_script("arguments[0].click();",download_sbis) # <--- Ищем вкладку скачать в footer
   time.sleep(2)
   
   sbis_plagin = main_page.find_download_plagin() # <--- Переходим в нужную вкладку
   sbis_plagin[1].click()
   
   find_download_link, download_text = main_page.find_download_block() 
   find_download_link.click() # <--- Скачиваем файл
   time.sleep(5)
   size = re.findall(r"[-+]?\d*\.\d+|\d+", download_text.text) # <--- Находим размер
   exe_files = glob.glob(f'{os.getcwd()}/*.exe') 
   file_size = round(os.path.getsize(exe_files[-1]) / 1048576, 2) # <--- Находим размер скаченного файла
      
   assert file_size == float(size[-1]), 'Different size' 
      
   os.remove(exe_files[-1])
