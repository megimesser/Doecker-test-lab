import json

path = "finance.json"
path_2 = "systemprompt.txt"
path_3 = "vanilla_prompt.txt"

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

data = json.dumps(data, indent=2)

with open(path_3, "r", encoding="utf-8") as f:
    data_2 = f.read()

prompt = data + "\n" + data_2

print(prompt)

with open(path_2, "w", encoding="utf-8") as b:
    b.write(prompt)