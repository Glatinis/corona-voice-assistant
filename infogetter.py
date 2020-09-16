import requests
from bs4 import BeautifulSoup

class Country:
    def __init__(self, c_id, name, t_cases, t_deaths, t_recovered):
    	self.id = c_id
    	self.name = name
    	self.t_cases = t_cases
    	self.t_deaths = t_deaths
    	self.t_recovered = t_recovered

def get_countries():
	page = requests.get('https://www.worldometers.info/coronavirus/#countries')
	soup = BeautifulSoup(page.text, 'html.parser')

	country_names = soup.find_all("a", {"class":"mt_a"})
	country_tags = []

	for country_name in country_names:
	    country = country_name.find_parent("tr")
	    country_tags.append(country)
	    if country_name.text == "China":
	        break

	countries = []

	countries.append(_create_world(soup))
	for country_tag in country_tags:
		countries.append(_create_country(country_tag))

	return countries

def _create_country(country_tag):
	c_txt = country_tag.text.split()
	c_id = c_txt[0]
	c_name = c_txt[1]
	c_cases = c_txt[2]
	c_deaths = c_txt[4]
	c_recovered = c_txt[6]

	print(c_id, c_name, c_cases, c_deaths, c_recovered)

	country = Country(c_id, c_name, c_cases, c_deaths, c_recovered)
	return country

def _create_world(soup):
	main_3 = soup.find_all("div", {"class":"maincounter-number"})

	w_id = 0
	name = "World"
	w_cases = main_3[0].text
	w_deaths = main_3[1].text
	w_recovered = main_3[2].text

	world = Country(w_id, name, w_cases, w_deaths, w_recovered)
	return world
