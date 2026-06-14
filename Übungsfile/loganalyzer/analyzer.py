import os 
from config import *
import re
import json



with open(LOG_DATA, "r") as f:
    log = f.read()

log = log.split("\n")

jsoni = {
    "gesamt": 0,
    "nach_level": {"INFO": 0, "ERROR": 0, "WARNING": 0, "CRITICAL": 0},
    "nach_user": {"Max": 0, "Peter": 0, "Laura": 0, "Günther": 0},
    "erster_critical": None
}


for lines in log:
        
        jsoni["gesamt"] += 1
        
        #Definition Message
        info = re.findall("INFO", lines)
        error = re.findall("ERROR", lines)
        warning = re.findall("WARNING", lines)
        critical = re.findall("CRITICAL", lines)

        if bool(info) == True: 
              jsoni["nach_level"]["INFO"] += 1
        elif bool(error) == True:
              jsoni["nach_level"]["ERROR"] += 1
        elif bool(warning) == True:
              jsoni["nach_level"]["WARNING"] += 1
        elif bool(critical) == True:
              jsoni["nach_level"]["CRITICAL"] += 1
        
              
        #Definition Namen
        Max = re.findall("Max", lines)
        Laura = re.findall("Laura", lines)
        Peter = re.findall("Peter", lines)
        Günther = re.findall("Günther", lines)


        if bool(Max) == True: 
              jsoni["nach_user"]["Max"] += 1
        elif bool(Laura) == True:
              jsoni["nach_user"]["Laura"] += 1
        elif bool(Peter) == True:
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

        
              



with open(JSONI, "w", encoding="utf-8") as f: 
      json.dump(jsoni,f,indent=4)
      
        



#print(json)



