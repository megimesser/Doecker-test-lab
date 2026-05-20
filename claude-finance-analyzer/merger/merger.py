from importer.importer import importer, format_portfolio
import json 

json_path = "finance.json"

def json_reader(path):
    return path


test = importer("finance.xlsx")
json_path = "finance.json"
formator= format_portfolio(test)

#print(formator)


with open(json_path, "r") as f:
        data = json.load(f)

#print(data)


for i in data:
     print(i["ticker"])
     
     




#print(type(formator))

for i in formator:
    for l in i:
        for s in data:
             if s["ticker"] == l:
                  print("gefunden")






def merger(formator, json_path):
    format = formator
    with open(json_path, "r") as f:
        data = json.load(f)

    #for key, value in data:
      #  key 
        

    return 


print(json_reader(json_path))


if __name__ == "__main__":
    #df = importer("finance.xlsx")
    #print(df.columns.tolist())
    #print(format_portfolio(df))
    print(json_reader(json_path))
   
