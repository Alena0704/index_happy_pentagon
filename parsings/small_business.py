from selenium import webdriver
import json
import time

DRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
url = 'https://riarating.ru/infografika/20200512/630169279.html'


def pars(url):
    file_name = "region.json"
    file_json = open (file_name, mode='w') 
    driver.get(url)
    time.sleep(2)
    url_places = driver.find_elements_by_css_selector(".table--1R1tF > tbody >tr")
    print(url_places)
    for region in url_places:
    	
        region_number = region.find_element_by_css_selector("td:nth-child(1)").text
        region_name = region.find_element_by_css_selector("td:nth-child(2)").text
        dolya_emp = region.find_element_by_css_selector("td:nth-child(3)").text
        oborot_one_emp_th_rub = region.find_element_by_css_selector("td:nth-child(4)").text
        oborot_milliard_rub = region.find_element_by_css_selector("td:nth-child(4)").text
        region = {
            'region_number':region_number,
            'region_name':region_name,
            'dolya_emp':dolya_emp,
            'oborot_one_emp_th_rub':oborot_one_emp_th_rub,
            'oborot_milliard_rub':oborot_milliard_rub
        }
        json.dump(region,file_json, ensure_ascii=False, sort_keys=True)
        print(region_number)
    file_json.close()   


pars(url)
