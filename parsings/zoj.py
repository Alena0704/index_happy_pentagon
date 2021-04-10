from selenium import webdriver
import json
import time

DRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
url = 'https://riarating.ru/infografika/20191001/630135852.html'


def pars(url):
    file_name = "region.json"
    file_json = open (file_name, mode='w') 
    driver.get(url)
    time.sleep(2)
    url_places = driver.find_elements_by_css_selector(".table--yNhWm > tbody >tr")
    print(url_places)
    for region in url_places:
    	
        region_number = region.find_element_by_css_selector("td:nth-child(1)").text
        region_name = region.find_element_by_css_selector("td:nth-child(2)").text
        region_reiting = region.find_element_by_css_selector("td:nth-child(3)").text
        region_ball = region.find_element_by_css_selector("td:nth-child(4)").text
        
        region = {
            'region_number':region_number,
            'region_name':region_name,
            'region_reiting':region_reiting,
            'region_ball':region_ball
        }
        json.dump(region,file_json, ensure_ascii=False, sort_keys=True)
        print(region_number)
    file_json.close()   


pars(url)
