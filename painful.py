'''
VVV Filters out a "dirty" version of a file of countries, removing empty lines and lines that say "Top of Page, as well as single characters of the alphabet"

import string
charsList = list(string.ascii_uppercase)
f = open("txttxt.txt", "r")
f2 = open("countriesRevised.txt", "w")
for line  in f.readlines():
    x = line.strip()
    if x != "Top of Page" and x != "" and x not in charsList:
        f2.write(line)

VVV Removes items from a list that do not belong as countries. VVV

f = open("countriesRevised.txt", "r")
allCountries = f.readlines()
unfilteredList = ["Portugal","Germany","Munster","Spain"]
filteredList = []
for line in allCountries:
    strippedLine = line.strip()
    if strippedLine in unfilteredList:
        filteredList.append(strippedLine)
print(filteredList)

'''




































