"""
Projektanforderungen
Konfigurationsdatei soll eingeelsen werden 


{
    "services": [
        {"name": "Google DNS", "url": "https://dns.google"},
        {"name": "GitHub API", "url": "https://api.github.com"},
        {"name": "httpbin", "url": "https://httpbin.org/get"}
        {"name": "test_wrong_statuscode", "url": "https://hiojpoijin.org/get"}
    ]
}


- Get Request an die oben stehenden services - 
- Antwortzeit soll gemessen werden 
- Try - Exceptblock für Timeout und Connection errors -> Service soll als down markiert werden 




/app/output/health_report.json form 


{
    "timestamp": "2026-05-09T10:30:00",
    "results": [
        {
            "name": "Google DNS",
            "url": "https://dns.google",
            "status": "UP",
            "status_code": 200,
            "response_time_ms": 45
        }
    ],
    "summary": {
        "total": 3,
        "up": 2,
        "down": 1
    }
}

services.json kommt per Bind Mount rein (Input vom Host)
health_report.json geht per Volume raus (Output persistent)
Diesmal brauchst du eine echte requirements.txt mit dem requests-Package
Setze ein Timeout von 5 Sekunden per Umgebungsvariable APP_TIMEOUT=5, die du per docker run -e übergibst und im Script über os.environ ausliest
Dein Dockerfile muss Layer-Caching-optimiert sein (requirements.txt separat kopieren)

Neue Python-Konzepte die du brauchst:

requests.get() mit timeout-Parameter
try/except für Exception Handling
time.time() für Zeitmessung
os.environ.get() mit Default-Wert
Dictionary-Verschachtelung (Dicts in Dicts in Listen)



"""
import json
import requests
import os 
from requests import status_codes
import datetime


#json function
#def json_ersteller():



timeout_parameter=int(os.environ.get("APP_TIMEOUT"))
print(timeout_parameter)


total=0
up=0
down=0


#Hülsenvariable json
daten = {}

# Formatvorlage json
results = {
    "timestamp": "Placeholder",
    "results": [
      
    ],
  
}



with open("app/services.json", "r", encoding="utf-8") as datei:
    daten = json.load(datei)

print(json.dumps(daten, indent=4, ensure_ascii=False))


#print(daten)





for n in daten["services"]: 
    url=n["url"]
    name=n["name"]
    total += 1
    #print(url)
    try:
        response = requests.get(url, timeout=timeout_parameter)
        print(response.status_code)
        status="UP"
        up +=1

        #print(response.elapsed.total_seconds())
        response_time = response.elapsed.total_seconds()
        response_time = str(response_time)[2:4]
        print(response_time)


        #If blöcke müssen in entsprechenden try block weil für exceptions eine exceptionklasse benötigt wird
        if response.status_code != 200:
            print(f"{name} is not reachable, statuscode: {response.status_code}")
            status="DOWN"
            down += 1
            print(response.status_code)

    
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        print(response.status_code)
        down += 1
        status="DOWN"
        

    except requests.exeception.Timeout:
        print(f"timeout for {name}")
        status="DOWN"
        down += 1
    finally:

        print("dicks")
        results["timestamp"]=str(datetime.datetime.now())
        results["results"].append({
            "name": str(name),
            "url": str(url),
            "status_code": response.status_code,
            "status": status,
            "response_time_ms": response_time  
        })
        



results["sumarry"] = {
            "total": total,
            "up": up,
            "down": down
        }



# In Jsonformat übersetzen und ausgeben 
with open("results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4)
