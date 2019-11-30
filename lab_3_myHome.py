import requests
import csv
from bs4 import BeautifulSoup

page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=1")
soup = BeautifulSoup(page.content, 'html.parser')
#print (soup.prettify())

#listings = soup.find("div", class_="PropertyListingCard")
#print (listings)

#price = listings.find(class_="PropertyListingCard__Price").text
#print (price)

#address = listings.find(class_="PropertyListingCard__Address").text
#print (address)

home_file = open('week03MyHome.csv', mode='w') 
home_writer = csv.writer(home_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

listings = soup.findAll("div", class_="PropertyListingCard" )


for listing in listings:
	entryList = []

	price = listing.find(class_="PropertyListingCard__Price").text
	entryList.append(price)
	address = listing.find(class_="PropertyListingCard__Address").text
	entryList.append(address)
	home_writer.writerow(entryList)
	
home_file.close()