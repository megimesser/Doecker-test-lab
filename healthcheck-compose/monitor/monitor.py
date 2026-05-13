import requests
import json
import os 

us = os.environ.get("APP_TIMEOUT")
us = int(us)

report = []

def request(link):
    r = requests.get(link, timeout=us)
    return r.status_code

with open("services.json", "r") as file:
    data = json.load(file)


for service in data["services"]:
    link = service["url"]
    #print(link)

    try:
        status = request(link)
    except requests.exceptions.RequestException as e:
        print("Fehler:", e)
        status = "error"

    report.append({
        "name": service["name"],
        "status": status
    })

print(report)

with open("health_report.json", "w") as file:
    json.dump(report, file, indent=4)

