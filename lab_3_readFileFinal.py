from bs4 import BeautifulSoup
import csv

with open("lab_2.html") as fp:
	soup = BeautifulSoup(fp,'html.parser')

#print (soup.tr)
employee_file = open('week02data.csv', mode='w')
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

rows = soup.findAll("tr")
for row in rows:

	cols = row.findAll("td", limit=3)
	dataList = []
	for col in cols:
		dataList.append(col.text)
	employee_writer.writerow(dataList)
employee_file.close()