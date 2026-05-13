import requests
import json 


with open("services.json", "r") as file:
    data = json.load(file)

print(data)


#def request():
#    r = requests.get()


blanko = {
    "services": [
        {"name": "API Health", "url": "http://api-server:5000/health"},
        {"name": "API Info", "url": "http://api-server:5000/info"},
        {"name": "Absichtlich kaputt", "url": "http://api-server:5000/nonexistent"}
    ]
}


print(len(blanko["services"]))
x = len(blanko["services"])

for i in blanko["services"]:
    #try 
    print(i["url"])