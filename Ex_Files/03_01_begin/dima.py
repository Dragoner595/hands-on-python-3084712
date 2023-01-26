import csv
from pprint import pprint

with open("TagniFiFundamentals-US0001593222-2022-10-23-2712.csv", "r") as f:
  read=csv.DictReader(f)
  searchs=list(read)

for search in searchs:
  if search["Q2-2022"] == "2022-06-30":
    pprint(search)
    break