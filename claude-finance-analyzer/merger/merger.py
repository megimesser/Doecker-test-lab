from importer.importer import importer, format_portfolio
import json 

json_path = "finance.json"

def json_reader(path):
    return path


test = importer("finance.xlsx")
json_path = "finance.json"
formator= format_portfolio(test)

print(formator)


with open(json_path, "r") as f:
        data = json.load(f)

#print(data)


for i in data:
     print(i["ticker"])
     
     


#print(type(formator))

# Loop durch die Exceldaten
for i in formator:
    #Loop durch die Dictionarys der Exceldaten
    for l in i:
        # Loop durch diee finance.json -> API Anfrage 
        for s in data:
             # Beim übereinstimmen der "ticker" welche in beiden Datensätzen vorhanden sind -> if Statement
             if s["ticker"] == l:
                  for number in i: 
                       if isinstance(number, float):
                              with open(json_path, "w") as f:
                                    json.dump(number, f, indent=4, ensure_ascii=False)

                            #print(f"{i} dick")
                  #with open(json_path, "w") as f:
                    #   json.dump







def merger(formator, json_path):
    format = formator
    with open(json_path, "r") as f:
        data = json.load(f)

    #for key, value in data:
      #  key 
        

    return 


#print(json_reader(json_path))


if __name__ == "__main__":
    #df = importer("finance.xlsx")
    #print(df.columns.tolist())
    #print(format_portfolio(df))
    print(json_reader(json_path))
   
