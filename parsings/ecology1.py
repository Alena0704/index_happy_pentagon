from selenium import webdriver
import json
import time

DRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
url = 'https://greenpatrol.ru/ru/stranica-dlya-obshchego-reytinga/ekologicheskiy-reyting-subektov-rf?tid=418'


def pars(url):
    file_name = "region.json"
    file_json = open (file_name, mode='w') 
    driver.get(url)
    time.sleep(2)
    url_places = driver.find_elements_by_css_selector(".views-table > tbody >tr")
    print(url_places)
    for region in url_places:
    	
        region_number = region.find_element_by_css_selector("td:nth-child(1)").text
        region_name = region.find_element_by_css_selector("td:nth-child(2)").text
        natural_security_index = region.find_element_by_css_selector("td:nth-child(3)").text
        industry_ecology_index = region.find_element_by_css_selector("td:nth-child(4)").text
        social_ecology_index = region.find_element_by_css_selector("td:nth-child(5)").text
        consolidated_index = region.find_element_by_css_selector("td:nth-child(6)").text
        region = {
            'region_number':region_number,
            'region_name':region_name,
            'natural_security_index':natural_security_index,
            'industry_ecology_index':industry_ecology_index,
            'social_ecology_index':social_ecology_index,
            'consolidated_index':consolidated_index,
        }
        json.dump(region,file_json, ensure_ascii=False, sort_keys=True)
        print(region_number)
    file_json.close()   


pars(url)
