#Projektanforderung 
#beim Start des Containers soll /app/logs/application.log eingelesen werden 
#jede Zeile soll nach den Parametern (INFO,WARNING,ERROR,CRITICAL) abgesucht werden 
#Auf Host soll sample.log mit den Logeintraägen existieren minimum 20 Zeilen
# Logdatei kommt per Bindmount in den Container

#Zusammenfassung nach /app/output/summary.json
# Summary kommt per Volume wieder raus 

#Wichtig zu befinn den Bindmount mit freigeben 
#docker run -v /app/logs/applica#Für das runnen des Containers : docker run -v /app/logs/:/app/logs/ logwatch:latest

import os
import re
import json 
from platform import platform
import subprocess

#Zusammenfassung der einzelnen logmeldungen in Zahlen 
warning=0
info=0
error=0
critical=0
times=0

#print(platform(aliased = True))

#path muss auf Dockercontainer angepasst werden
path = os.path.expanduser("/app/logs/sample.log")

with open(path, "r", encoding="utf-8") as f:
    for line in f:
        if re.search(".*ERROR.*$", line):
            error+=1
            times+=1
        elif re.search(".*INFO.*$", line):
            info+=1
            times+=1
        elif re.search(".*CRITICAL.*$", line):
            critical+=1
            times+=1
        elif re.search(".*WARNING.*$", line):
            warning+=1
            times+=1



#print(f"errors in file {error}")
#print(f"info in file {info}")
#print(f"critical in file {critical}")
#print(f"warning in file {warning}")
#print(times)



daten= {
    "ERROR":error,
    "WARNING":warning,
    "INFO":info,
    "CRITICAL":critical,
}


with open("summary.json", "w", encoding="utf-8") as datei:
    json.dump(daten, datei, indent=4, ensure_ascii=False)




result = subprocess.run(
    "cp summary.json /app/logs/json",
    shell=True,
    capture_output=True,
    text=True
)

print(result.stdout)









#print(content)


