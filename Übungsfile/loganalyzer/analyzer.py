import os 
from config import *
import re
import json
import argparse





with open(LOG_DATA, "r") as f:
    log = f.read()

log = log.split("\n")

jsoni = {
    "gesamt": 0,
    "nach_level": {"INFO": 0, "ERROR": 0, "WARNING": 0, "CRITICAL": 0},
    "nach_user": {"Max": 0, "Peter": 0, "Laura": 0, "Günther": 0},
    "erster_critical": None
}


parser = argparse.ArgumentParser(description="Analysiert app.log")
# Parser ist ein Objekt und wird mit den Instanzvariablen instanziiert


parser.add_argument(
      "--level",
      help="nur dieses Log_Level zählen"
      )

parser.add_argument(
      "--user",
      help="nur Messages dieses Users zählen"
)

parser.add_argument(
      "--output",
      help="Outputpfad des Files"
      
)

#Was macht parser.add
# Parser - objekt
# add_argument - Objectmethod aus der argparse class

args = parser.parse_args()
# Was macht parse_args()?
#Liest die Argumente aus der Kommandozeile (sys.argv)
#Prüft sie anhand der Definitionen aus add_argument()
#Wandelt sie ggf. in die angegebenen Typen um (int, float, ...)
#Speichert sie in einem Objekt (Namespace)
#Gibt dieses Objekt zurück







for lines in log:
        
        jsoni["gesamt"] += 1
        
        #Definition Message
        
        info = re.findall("INFO", lines)
        error = re.findall("ERROR", lines)
        warning = re.findall("WARNING", lines)
        critical = re.findall("CRITICAL", lines)

        if bool(info) == True and args.level == "INFO": 
              jsoni["nach_level"]["INFO"] += 1
              jsoni["nach_level"]["ERROR"] = None
              jsoni["nach_level"]["WARNING"] = None
              jsoni["nach_level"]["CRITICAL"] = None
        elif bool(error) == True and args.level == "ERROR":
              jsoni["nach_level"]["ERROR"] += 1
              jsoni["nach_level"]["WARNING"] = None
              jsoni["nach_level"]["CRITICAL"] = None
              jsoni["nach_level"]["INFO"] = None
        elif bool(warning) == True and args.level == "WARNING":
              jsoni["nach_level"]["WARNING"] += 1
              jsoni["nach_level"]["CRITICAL"] = None
              jsoni["nach_level"]["INFO"] = None
              jsoni["nach_level"]["ERROR"] = None
        elif bool(critical) == True and args.level == "CRITICAL":
              jsoni["nach_level"]["CRITICAL"] += 1
              jsoni["nach_level"]["INFO"] = None
              jsoni["nach_level"]["ERROR"] = None
              jsoni["nach_level"]["WARNING"] = None
        else: 
              jsoni["nach_level"]["CRITICAL"] += 1
              jsoni["nach_level"]["WARNING"] += 1
              jsoni["nach_level"]["ERROR"] += 1
              jsoni["nach_level"]["INFO"] += 1
        
              
        #Definition Namen
        Max = re.findall("Max", lines)
        Laura = re.findall("Laura", lines)
        Peter = re.findall("Peter", lines)
        Günther = re.findall("Günther", lines)

# Problem die erste Schleife springt nur an wenn ein Level angegeben wird 
        if bool(Max) == True and args.user == "Max": 
              jsoni["nach_user"]["Max"] += 1
        elif bool(Laura) == True and args.user == "Laura":
              jsoni["nach_user"]["Laura"] += 1
        elif bool(Peter) == True and args.user == "Peter":
              jsoni["nach_user"]["Peter"] += 1
        elif bool(Günther) == True:
              jsoni["nach_user"]["Günther"] += 1

        Critical = re.findall("CRITICAL", lines)

        stringer = ""

        if jsoni["erster_critical"] == None:
            if Critical: 
                splitter = lines.split()
                #print(splitter[0], splitter[1])
                stringer += splitter[0]
                stringer += " "
                stringer += splitter[1]
                jsoni["erster_critical"] = stringer
                #print(stringer)

if args.user:
            print(f"{jsoni["nach_user"][args.user]}")
if args.level: 
            print(f"{jsoni["nach_level"][args.level]}")
              



with open(JSONI, "w", encoding="utf-8") as f: 
      json.dump(jsoni,f,indent=4)
      
        



#print(json)



