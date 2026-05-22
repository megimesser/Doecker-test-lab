from importer.importer import importer, format_portfolio
import json 

json_path = "finance.json"

def json_reader(path):
    return path


test = importer("finance.xlsx")
json_path = "finance.json"
formator= format_portfolio(test)

#print(formator)


def merger(json_path,formator):
#print(type(formator))

    # 1. JSON einlesen
    with open(json_path, "r") as f:
        data = json.load(f)

    # 2. Für jeden API-Eintrag den passenden Excel-Eintrag finden

    #Iteration durch die API Json
    for stock in data:
        # Iteration durch die Excel
        for excel_row in formator:
            # Wenn der Ticker der Excel die der Json matcht
            if stock["ticker"] in excel_row:
                # Iteration durch die Exceldictionarys nach dem Value
                for value in excel_row:
                    if isinstance(value, float):
                        #Zugriff auf Eigenkapitalfeld 
                        stock["Eigenkapital"] = value
                        break

    # 3. Zurückschreiben
    with open(json_path, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    f = "merge abgeschlossen"
    return f




"""

def merger(formator, json_path):
    format = formator
    with open(json_path, "r") as f:
        data = json.load(f)

    #for key, value in data:
      #  key 
        

    return 
"""

#print(json_reader(json_path))


if __name__ == "__main__":
    #df = importer("finance.xlsx")
    #print(df.columns.tolist())
    #print(format_portfolio(df))
    #print(json_reader(json_path))
    print(merger(json_path,formator))
   
