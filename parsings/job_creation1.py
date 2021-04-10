from selenium import webdriver
import json
import time

DRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
url = 'https://riarating.ru/infografika/20190416/630123400.html'


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
        number_of_jobs_3_years = region.find_element_by_css_selector("td:nth-child(3)").text
        number_of_jobs_10_years = region.find_element_by_css_selector("td:nth-child(4)").text
        change_number_jobs_3_years = region.find_element_by_css_selector("td:nth-child(5)").text
        change_number_jobs_10_years = region.find_element_by_css_selector("td:nth-child(5)").text
        region = {
            'region_number':region_number,
            'region_name':region_name,
            'number_of_jobs_3_years':number_of_jobs_3_years,
            'number_of_jobs_10_years':number_of_jobs_10_years,
            'change_number_jobs_3_years':change_number_jobs_3_years,
            'change_number_jobs_10_years':change_number_jobs_10_years,
        }
        json.dump(region,file_json, ensure_ascii=False, sort_keys=True)
        print(region_number)
    file_json.close()   


pars(url)
