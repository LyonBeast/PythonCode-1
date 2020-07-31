import requests

r = requests.get("http://www.pythonhow.com/data/universe.txt:")
print(r.text)
