from config import JSON_FILE
import json

with open(JSON_FILE,"r") as f:
    x = json.load(f)

print(x)