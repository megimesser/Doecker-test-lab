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


zwischenspeicher = zwischenspeicher.split()

with open("test.txt", "w") as f:
    for i in zwischenspeicher:
        i = i.strip()  # entfernt Leerzeichen + \n
        if i.startswith("APP_"):
            f.write(i + "\n")
            print(i)





