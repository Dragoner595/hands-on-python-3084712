import csv
from pprint import pprint
from datetime import datetime
#now we will make open scv fıle wıth python lıberary
with open('laureates.csv','r') as f:
  read=csv.DictReader(f)
  calculations=list(read)
#we will write calculation formula to calculate his age 
for calculation in calculations:
  if calculation["surname"] == "Einstein":
    pprint(calculation)
    print('----------------')
    diedDate = datetime.strptime(calculation['died'],'%Y-%m-%d')
    birtDate = datetime.strptime(calculation['born'],'%Y-%m-%d')
    yearDate = datetime.strptime(calculation['year'],'%Y')
    print("Years past after Laureate to death", (diedDate.year-birtDate.year)-(yearDate.year-birtDate.year))
    break
