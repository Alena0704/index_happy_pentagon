from selenium import webdriver
import json
import time
import apache_beam as beam
DRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
url_popuation = 'https://riarating.ru/infografika/20210405/630198230.html'
url_salary = 'https://riarating.ru/infografika/20210330/630197606.html'
url_oil = 'https://riarating.ru/infografika/20210209/630194414.html'
url_dtp = 'https://riarating.ru/infografika/20201110/630190310/Reyting-regionov-RF-po-avariynosti-na-dorogakh-za-9-mesyatsev-2020-goda.html'
url_unempl = 'https://riarating.ru/infografika/20210316/630196679.html'
url_crime = ''
url_living = ''
url_min = ''
url_index_happy = 'https://riarating.ru/infografika/20210216/630194637.html'
url_work = 'https://riarating.ru/infografika/20200908/630179386.html'
url_budget = 'https://riarating.ru/infografika/20190528/630125306.html'

def parsing(feature):
    if feature == 'population':
	    url = url_population
	    driver.get(url)
	    time.sleep(2)
	    population_lst = []
	    url_places = driver.find_elements_by_css_selector(".table--2HjiB > tbody >tr")
	    #print(url_places)
	    for region in url_places:
		region_number = region.find_element_by_css_selector("td:nth-child(1)").text
		region_name = region.find_element_by_css_selector("td:nth-child(2)").text
		profit_minus_population = region.find_element_by_css_selector("td:nth-child(3)").text
		hislenost_1_jan = region.find_element_by_css_selector("td:nth-child(4)").text
		etstven_prirost_ubyl_2016_2018 = region.find_element_by_css_selector("td:nth-child(5)").text
		region = {
		    'region_number':region_number,
		    'region_name':region_name,
		    'profit_minus_population':profit_minus_population,
		    'hislenost_1_jan':hislenost_1_jan,
		    'etstven_prirost_ubyl_2016_2018':etstven_prirost_ubyl_2016_2018
		}
		population_lst.append(region)
		yield ({'type':'population','datas': region})
		#json.dump(region,file_json, ensure_ascii=False, sort_keys=True)
	    #file_json.close()
	    print('population done')
	    
    if feature == 'salary':
	    url = url_salary
	    driver.get(url)
	    time.sleep(2)
	    salary_lst = []
	    url_places = driver.find_elements_by_css_selector(".table--l6yoJ > tbody >tr")
	    #print(url_places)
	    for region in url_places:
	    	
		region_number = region.find_element_by_css_selector("td:nth-child(1)").text
		region_name = region.find_element_by_css_selector("td:nth-child(2)").text
		dolya_region_employees = region.find_element_by_css_selector("td:nth-child(3)").text
		mean_salary = region.find_element_by_css_selector("td:nth-child(4)").text
		profit = region.find_element_by_css_selector("td:nth-child(5)").text
		ratio_sm_me = region.find_element_by_css_selector("td:nth-child(5)").text
		region = {
		    'region_number':region_number,
		    'region_name':region_name,
		    'dolya_region_employees':dolya_region_employees,
		    'mean_salary':mean_salary,
		    'profit':profit,
		    'ratio_sm_me':ratio_sm_me
		}
		salary_lst.append(region)
		yield ({'type':'salary','datas':region})
		#json.dump(region,file_json, ensure_ascii=False, sort_keys=True)
		#print(region_number)
	    #file_json.close()
	    print('salary done')
	    
    if feature == 'oil':
    	url = url_oil
	driver.get(url)
	time.sleep(2)
	url_places = driver.find_elements_by_css_selector(".table--3ATai > tbody")
	#print(url_places)
	oil_lst = []
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
		oil_lst.append(region)
		yield ({'type':'oil','datas': region})
	print('oil done')
	
    if feature == 'dtp':
	    url = url_dtp
	    driver.get(url)
	    time.sleep(2)
	    dtp_lst = []
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
		    'kolvo_avaria_100k_auto':kolvo_avaria_100k_auto,
		    'izmen_dtp_2018':izmen_dtp_2018,
		    'chislo_postradavshih_100k_2019':chislo_postradavshih_100k_2019,
		    'chislo_pogib_100k_postradavsh':chislo_pogib_100k_postradavsh
		}
		#json.dump(region,file_json, ensure_ascii=False, sort_keys=True)
		#print(region_number)
		dtp_lst.append(region)
		yield ({'type':'dtp', 'datas': region})
	    #file_json.close()
	    print('dtp done')

    if feature == 'unempl':
	    url = url_unempl
	    driver.get(url)
	    time.sleep(2)
	    unempl_lst = []
	    url_places = driver.find_elements_by_css_selector(".table--3ybP0 > tbody >tr")
	    #print(url_places)
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
		unempl_lst.append(region)
		#json.dump(region,file_json, ensure_ascii=False, sort_keys=True)
		#print(region_number)
		yield ({'type':'unempl', 'datas': region})
	    #file_json.close()
	    print('unemployment done')
    
    if feature == 'index_happy':
	    url = url_index_happy
	    driver.get(url)
	    time.sleep(2)
	    lst_ind = []
	    url_places = driver.find_elements_by_css_selector(".table--3tR69 > tbody >tr")
	    #print(url_places)
	    for region in url_places:
	    	
		region_number = region.find_element_by_css_selector("td:nth-child(1)").text
		region_name = region.find_element_by_css_selector("td:nth-child(2)").text
		region_reiting_ball = region.find_element_by_css_selector("td:nth-child(3)").text
		region_mesto_2019 = region.find_element_by_css_selector("td:nth-child(4)").text
		region = {
		    'region_number':region_number,
		    'region_name':region_name,
		    'region_reiting_ball':region_reiting_ball,
		    'region_mesto_2019':region_mesto_2019
		}
		lst_ind.append(region)
		yield ({'type':'index_happy','datas': region})
		#print(region_number)
	    print('index_happy done')

    if feature == 'work':
	    url = url_work
	    driver.get(url)
	    time.sleep(2)
	    lst_ind = []
	    url_places = driver.find_elements_by_css_selector(".table--YVue4 > tbody >tr")
	    #print(url_places)
	    for region in url_places:
	    	
		region_number = region.find_element_by_css_selector("td:nth-child(1)").text
		region_name = region.find_element_by_css_selector("td:nth-child(2)").text
		region_index = region.find_element_by_css_selector("td:nth-child(3)").text
		region_index_2019 = region.find_element_by_css_selector("td:nth-child(4)").text
		region = {
		    'region_number':region_number,
		    'region_name':region_name,
		    'region_index':region_index,
		    'region_index_2019':region_index_2019
		}
		lst_ind.append(region)
		yield ({'type':'work', 'datas': region})
		#print(region_number)
	    print('work done')
    if feature == 'budget':
            url = url_budget
	    driver.get(url)
	    time.sleep(2)
	    lst_ind = []
	    url_places = driver.find_elements_by_css_selector(".table--2HjiB > tbody >tr")
	    #print(url_places)
	    for region in url_places:
	    	
		region_number = region.find_element_by_css_selector("td:nth-child(1)").text
		region_name = region.find_element_by_css_selector("td:nth-child(2)").text
		region_rash = region.find_element_by_css_selector("td:nth-child(3)").text
		region_rash_2019 = region.find_element_by_css_selector("td:nth-child(4)").text
		region_dolya_2019 = region.find_element_by_css_selector("td:nth-child(5)").text
		region = {
		    'region_number':region_number,
		    'region_name':region_name,
		    'region_rash':region_rash,
		    'region_rash_2019':region_rash_2019,
		    'region_dolya_2019':region_dolya_2019
		}
		lst_ind.append(region)
		yield ({'type': 'budget', 'datas': region})
	    print('society done')
import mysql.connector
mydb = mysql.connector.connect(host = "hosthere.tech", user = "root", password = "password", database = "index_happy")
mycursor = mydb.cursor()

def go_to_bd(feature):
    res = mycursor.execute("select id_regions from regions where name = {}".format(feature['datas']['region_name']))
    id_ = res[0]
    if feature['type'] == 'population':
    	str_ = "insert into population (id_regions, year, value) values (%s, %s, %s)"
    	mycursor.execute(str_, (id_, '2021', feature['datas']['hislenost_1_jan']))
    elif feature['type'] == 'salary':
    	str_ = "insert into mean_salary (id_regions, year, value) values (%s, %s, %s)"
    	mycursor.execute(str_, (id_, '2021', feature['datas']['mean_salary']))
    elif feature['type'] == 'oil':
    	str_ = "insert into fuel (id_regions, year, value_92) values (%s, %s, %s)"
    	mycursor.execute(str_, (id_, '2021', feature['datas']['region_cost']))
    elif feature['type'] == 'dtp':
    	str_ = "insert into traffic_axident (id_regions, year, value_100000,value_dead ) values (%s, %s, %s, %s)"
    	mycursor.execute(str_, (id_, '2021', feature['datas']['kolvo_avaria_100k_auto'], feature['datas'['chislo_pogib_100k_postradavsh']))
    elif feature['type'] == 'unempl':
    	str_ = "insert into unemployment_rate (id_regions, year, value) values (%s, %s, %s)"
    	mycursor.execute(str_, (id_, '2021', feature['datas']['level_unemployment']))
    elif feature['type'] == 'index_happy':
    	str_ = "insert into index_happy (id_regions, year, value) values (%s, %s, %s)"
    	mycursor.execute(str_, (id_, '2021', feature['datas']['region_reiting_ball']))
    elif feature['type'] == 'work':
    	str_ = "insert into index_work (id_regions, year, value) values (%s, %s, %s)"
    	mycursor.execute(str_, (id_, '2021', feature['datas']['region_index']))
    elif feature['type'] == 'budget':
    	str_ = "insert into social_budget (id_regions, year, value) values (%s, %s, %s)"
    	mycursor.execute(str_, (id_, '2021', feature['datas']['region_rash']))
    	
def run_beam(lst):
    for i in lst:
    	with beam.Pipeine() as p:
    	    (p | beam.Map(parsing)
    	       | beam.ParDo(go_to_bd)

lst = ['population', 'salary', 'oil','dtp', 'unemploment', 'index_happy', 'index_work', 'society']
for i in lst:
    go_to_bd(i)

