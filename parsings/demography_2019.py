from selenium import webdriver
import json
import time

DRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
url = 'https://riarating.ru/infografika/20190423/630123908.html'


def pars(url):
    file_name = "region.json"
    file_json = open (file_name, mode='w') 
    driver.get(url)
    time.sleep(2)
    url_places = driver.find_elements_by_css_selector(".table--2HjiB > tbody >tr")
    print(url_places)
    for region in url_places:
    	
        region_number = region.find_element_by_css_selector("td:nth-child(1)").text
        region_name = region.find_element_by_css_selector("td:nth-child(2)").text
        profit_minus_population = region.find_element_by_css_selector("td:nth-child(3)").text
        hislenost_1_jan = region.find_element_by_css_selector("td:nth-child(4)").text
        etstven_prirost_ubyl_2016_2018 = region.find_element_by_css_selector("td:nth-child(5)").text
        migracia = region.find_element_by_css_selector("td:nth-child(6)").text
        region = {
            'region_number':region_number,
            'region_name':region_name,
            'profit_minus_population':profit_minus_population,
            'hislenost_1_jan':hislenost_1_jan,
            'etstven_prirost_ubyl_2016_2018':etstven_prirost_ubyl_2016_2018
        }
        json.dump(region,file_json, ensure_ascii=False, sort_keys=True)
        print(region_number)
    file_json.close()   


pars(url)
