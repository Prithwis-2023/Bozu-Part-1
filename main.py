print("<-------------------Part 1(1)------------------->")
from bs4 import BeautifulSoup
import requests
import csv
from csv import writer
data = requests.get("https://en.wikipedia.org/wiki/Donald_Trump")
data = str(data)
print(f"Webpage Response Code:", data[11:14])
data2 = requests.get("https://en.wikipedia.org/wiki/Donald Trump").text
soup = BeautifulSoup(data2, 'lxml')
title = soup.find('h1', class_="firstHeading").text
print("Title of the Webpage: ", title)
print("Html Code of the Webpage\n<----------------------------------------------------------------------------->")
print(soup.prettify())
print("<-------------------------------------------------------------------------------------->")
file = open('details.csv')
csv_f = csv.reader(file)
list_details = []
name = soup.find('div', class_="fn").text
list_details.append(name)
birth_name = soup.find('div', class_="nickname").text
list_details.append(birth_name)
dob = soup.find('span', class_='bday').text
list_details.append(dob)
age = soup.find('span', class_='noprint ForceAgeToShow').text
age = str(age)
list_details.append(age[6:8])
data_full = soup.find_all('span', class_='noprint')
birth_place = data_full[0].parent.get_text()
list_details.append(birth_place[53:])
party_full = soup.find_all('th', class_='infobox-label')
party_reduced = party_full[4].parent.get_text()
list_details.append(party_reduced[15:25])
with open('details.csv', 'a') as f:
    writer_object = writer(f)
    writer_object.writerow(list_details)
    f.close()
  


