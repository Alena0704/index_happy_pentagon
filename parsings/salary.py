from selenium import webdriver
import json
import time

DRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
url = 'https://riarating.ru/infografika/20191202/630143771.html'


def pars(url):
    file_name = "region.json"
    file_json = open (file_name, mode='w') 
    driver.get(url)
    time.sleep(2)
    url_places = driver.find_elements_by_css_selector(".table--l6yoJ > tbody >tr")
    print(url_places)
    for region in url_places:
    	
        region_number = region.find_element_by_css_selector("td:nth-child(1)").text
        region_name = region.find_element_by_css_selector("td:nth-child(2)").text
        dolya_region_employees_100 = region.find_element_by_css_selector("td:nth-child(3)").text
        dolya_region_employees_15 = region.find_element_by_css_selector("td:nth-child(4)").text
        median_salary = region.find_element_by_css_selector("td:nth-child(5)").text
        most_common_salaries = region.find_element_by_css_selector("td:nth-child(5)").text
        region = {
            'region_number':region_number,
            'region_name':region_name,
            'dolya_region_employees_100':dolya_region_employees_100,
            'dolya_region_employees_15':dolya_region_employees_15,
            'median_salary':median_salary,
            'most_common_salaries':most_common_salaries
        }
        json.dump(region,file_json, ensure_ascii=False, sort_keys=True)
        print(region_number)
    file_json.close()   


pars(url)
