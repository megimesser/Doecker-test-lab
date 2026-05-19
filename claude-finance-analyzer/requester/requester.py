import requests
import os
import json
import time
from importer.importer import importer


#Nach test löschen 
api_key=os.getenv("CLAUDE_KEY")


with open("systemprompt.txt", "r") as message:
    content = message.read()
    content = str(content)

#Message print 
#print(content)

try:
    response = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": api_key,
            "content-type": "application/json",
            "anthropic-version": "2023-06-01"
        },
        json={
            "model": "claude-sonnet-4-6",
            "max_tokens": 1500,
            "tools": [
                {
                    "type": "web_search_20250305",
                    "name": "web_search"
                }
            ],
            "messages": [
                {"role": "user", "content": content}
            ]
        }
    )

    print(f"Status: {response.status_code}")

    
    if response.status_code != 200:
        print(f"API Error: {response.json()}")
        exit(1)
except:
    
data = response.json()

# Alle Text-Blöcke zusammensammeln (Web Search erzeugt mehrere Blöcke)
antwort = ""
for block in data["content"]:
    if block["type"] == "text":
        antwort += block["text"]

print(antwort)

with open("output.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

with open("antwort.txt", "w", encoding="utf-8") as file:
    file.write(antwort)



#time.sleep(20)
import sender
sender.sender()

