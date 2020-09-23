'''
import requests
f = requests.get("http://www.pythonhow.com/data/sampledata.txt", "r", headers = {'user-agent': 'customUserAgent'})
f2 = requests.get("http://www.pythonhow.com/data/sampledata_x_2.txt", "r", headers = {'user-agent': 'customUserAgent'})
fText = f.text
f2Text = f2.text
No_U = open("fileButBetter.txt", "w+")
No_U.writelines(fText + "\n")
f2List = f2Text.split("\n")
for line in f2List:
    if line == "x,y":
        continue
    No_U.write(line + "\n")
'''
import pandas
 
data1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = pandas.read_csv("http://www.pythonhow.com/data/sampledata_x_2.txt")
data12 = pandas.concat([data1, data2])
data12.to_csv("fileButBetter.txt", index=None)
