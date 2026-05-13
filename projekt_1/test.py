from datetime import datetime
import subprocess
import os

#Datetime
now = datetime.now()
print(now)


#Hostname 
result = subprocess.run(["hostname"], capture_output=True, text=True)
print(result.stdout)





#Environmentvariablen
path = os.path.expanduser("~/.zshrc")
result = subprocess.run(["cat", path], capture_output=True, text=True)
zwischenspeicher=result.stdout



# Problem - ein Dockercontainer hat keine zshrc - meistens eine bashrc - dies muss entsprechend beachtet werden 
# Problem nummer 2 - Docker greift auf Umgebungsvariablen mit os.environ zu und nicht über path.exapnduser 


for key, value in os.environ.items():
    if key.startswith("APP_"):
        print(f"{key}={value}")


# Innerhalb des Containers muss die workingdir erstellt werden dies geschieht über das Script
os.makedirs("/app/output", exist_ok=True)
with open("/app/output/report.txt", "w") as f:
    # schreiben




#Speichern in report.txt -- wichtig /app/... lässt sich nicht auf dem Host erstellen
zwischenspeicher = zwischenspeicher.split()

with open("test.txt", "w") as f:
    for i in zwischenspeicher:
        i = i.strip()  # entfernt Leerzeichen + \n
        if i.startswith("APP_"):
            f.write(i + "\n")
            print(i)






