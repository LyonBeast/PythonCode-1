import requests

f2 = open("filefile.txt", "w+")
response = requests.get("http://www.pythonhow.com/data/sampledata.txt", headers = {'user-agent': 'customUserAgent'})
response = response.text
responseList = response.split("\n")
for line in responseList:
    if line == "x,y":
        f2.write(line + ' ')
        continue
    else:
        x,y = line.split(",")
        x = int(x) * 2
        y = int(y) * 2
    twoNumbers = str(x) + "," + str(y) + " " + "\n"
    f2.write(twoNumbers)
print(f2.readlines())
f2.close()
        
 