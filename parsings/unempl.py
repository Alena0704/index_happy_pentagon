from selenium import webdriver
import json
import time

DRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
url = 'https://riarating.ru/infografika/20200317/630157723.html'


def pars(url):
    file_name = "region.json"
    file_json = open (file_name, mode='w') 
    driver.get(url)
    time.sleep(2)
    url_places = driver.find_elements_by_css_selector(".table--3ybP0 > tbody >tr")
    print(url_places)
    for region in url_places:
    	
        region_number = region.find_element_by_css_selector("td:nth-child(1)").text
        region_name = region.find_element_by_css_selector("td:nth-child(2)").text
        level_unemployment = region.find_element_by_css_selector("td:nth-child(3)").text
        change_level = region.find_element_by_css_selector("td:nth-child(4)").text
        number_of_unemployed = region.find_element_by_css_selector("td:nth-child(5)").text
        average_time = region.find_element_by_css_selector("td:nth-child(6)").text
        region = {
            'region_number':region_number,
            'region_name':region_name,
            'level_unemployment':level_unemployment,
            'change_level':change_level,
            'number_of_unemployed':number_of_unemployed,
            'average_time':average_time
        }
        json.dump(region,file_json, ensure_ascii=False, sort_keys=True)
        print(region_number)
    file_json.close()   


pars(url)
