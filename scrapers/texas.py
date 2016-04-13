import csv
import requests 
from BeautifulSoup import BeautifulSoup

url = 'http://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html'

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

table = soup.findAll('table')[0]

list_of_rows = []
for row in table.findAll('tr')[1:]:
    list_of_cells = []
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text)
        if cell.find('a'):
            list_of_cells.append("http://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html" + cell.find('a')['href'])
    list_of_rows.append(list_of_cells)
	
outfile = open("./executions.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(['Scheduled Execution', 'Offender Information', 'Link', 'Last Name', 'First Name', 'TDCJ No.', 'Birth Date', 'Race', 'Date Received', 'County'])
writer.writerows(list_of_rows)