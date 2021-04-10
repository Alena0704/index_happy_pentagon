from selenium import webdriver
import json
import time

DRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
url = 'https://riarating.ru/infografika/20200225/630154531.html'


def pars(url):
    file_name = "region.json"
    file_json = open (file_name, mode='w') 
    driver.get(url)
    time.sleep(2)
    url_places = driver.find_elements_by_css_selector(".table--2Tft7 > tbody >tr")
    #print(url_places)
    for region in url_places:
    	
        region_number = region.find_element_by_css_selector("td:nth-child(1)").text
        region_name = region.find_element_by_css_selector("td:nth-child(2)").text
        kolvo_avaria_100k_auto = region.find_element_by_css_selector("td:nth-child(3)").text
        izmen_dtp_2018 = region.find_element_by_css_selector("td:nth-child(4)").text
        chislo_postradavshih_100k_2019 = region.find_element_by_css_selector("td:nth-child(5)").text
        chislo_pogib_100k_postradavsh = region.find_element_by_css_selector("td:nth-child(6)").text
        region = {
            'region_number':region_number,
            'region_name':region_name,
            'region_volume':kolvo_avaria_100k_auto,
            'region_cost':izmen_dtp_2018,
            'region_change':chislo_postradavshih_100k_2019,
            'region_change':chislo_pogib_100k_postradavsh
        }
        json.dump(region,file_json, ensure_ascii=False, sort_keys=True)
        print(region_number)
    file_json.close()   


pars(url)
