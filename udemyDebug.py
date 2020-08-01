'''
import string
f = open("twochar.txt", 'w')
counter = 0
byTwos = ""
currentLine = ''
listchar = list(map(str, string.ascii_lowercase))
for x in listchar:
  byTwos += x
  if counter % 3 != 0:  
    f.write(byTwos + "\n")
    byTwos = ''
  counter += 1

f.close()


import string 
f = open('twochar.txt', 'w')
byTwos = ""
currentLine = ""
listchar = list(map(str, string.ascii_lowercase))
for x in range(1,(len(listchar) + 1)):
  byTwos += listchar[x - 1]
  if x % 2 == 0:
    f.write(byTwos + "\n")
    byTwos = ""
f.close()



import string
alphabet = list(map(str, string.ascii_lowercase))
fileName = ""
for x in alphabet:
  fileName += x
  fileName += ".txt"
  f = open(fileName, 'w')
  f.write(x)
  f.close()
  fileName = ""

import string 
f = open('twochar.txt', 'w')
byTwos = ""
currentLine = ""
listchar = list(map(str, string.ascii_lowercase))
for x in range(1,(len(listchar) + 1)):
  byTwos += listchar[x - 1]
  if (x + 1) % 3 == 0:
    f.write(byTwos + "\n")
    byTwos = ""
f.write(byTwos)
f.close()

import string
def alphabetLines(charLine):
  charLine = int(charLine)
  f = open('twochar.txt', 'w')
  byLines = ""
  alphaList = list(map(str, string.ascii_lowercase))
  for x in range(0, len(alphaList)):
    byLines += alphaList[x]
    if (x + 1) % charLine == 0:
      f.write(byLines + "\n")
      byLines = ""
  if byLines != "":
    f.write(byLines)
    f.close()
    return "File should be updated. Please check."

print(alphabetLines(4))



import json
str_employee = '{"employees":[{"firstName": "John", "lastName": "Doe"},{"firstName": "Anna", "lastName": "Smith"},{"firstName": "Peter", "lastName": "Jones"}],"owners":[{"firstName": "Jack", "lastName": "Petter"},{"firstName": "Jessy", "lastName": "Petter"}]}'

employee_obj = json.loads(str_employee)

#d["employees"].append(dict(firstName = "Jason", lastName = "Wang"))

with open("twochar.txt", "w") as thingyInA_File:
  thingyInA_File.write(json.dumps(d,thingyInA_File))




iLikeCats = ["Meow", "Mew", "Purr"]
for counter, sound in enumerate(iLikeCats):
  print(sound + " has index " + str(counter))



'''



print("using git now")




























