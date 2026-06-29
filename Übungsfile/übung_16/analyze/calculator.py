from data.loader import open_json
from config import JSON_FILE




def run_analyse(liste):
    dic = {
        "gesamtumsatz" : 0,
        "bestseller" : "",
        "anzahl_produkte": 0
    }

    f = 0

    best = max(liste, key=lambda s: s["menge"])
    dic["bestseller"] = best["produkt"]

    for i in liste:
        x = i["menge"]
        dic["gesamtumsatz"] = i["menge"] *  i["preis"]
        if x > f: 
            f = x
            dic["anzahl_produkte"] = i["menge"]
            #dic["bestseller"] = i["produkt"]

        
        
    
    return dic
    
    #return print(liste)
    



if __name__ == "__main__":
    x = run_analyse(open_json(JSON_FILE))
    print(x)