from selenium import webdriver
import json
import time

DRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
url = 'https://riarating.ru/infografika/20200211/630153374.html'

def pars(url):
	file_name = "region.json"
	file_json = open (file_name, mode='w')
	driver.get(url)
	time.sleep(2)
	url_places = driver.find_elements_by_css_selector(".table--3ATai > tbody")
	print(url_places)
	for region in url_places:
		region_number = driver.find_element_by_css_selector("tr>td:nth-child(1)").text
		region_name = driver.find_element_by_css_selector("tr>td:nth-child(2)").text
		region_volume = driver.find_element_by_css_selector("tr>td:nth-child(3)").text
		region_cost = driver.find_element_by_css_selector("tr>td:nth-child(4)").text
		region_change = driver.find_element_by_css_selector("tr>td:nth-child(5)").text
		region = {
			'region_number':region_number,
			'region_name':region_name,
			'region_volume':region_volume,
			'region_cost':region_cost,
			'region_change':region_change
			}
	json.dump(region,file_json)
	print(region_number)
	file_json.close()

	pars(url)
