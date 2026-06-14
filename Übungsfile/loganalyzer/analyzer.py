import os 
from config import *
import re

f = LOG_DATA



with open(LOG_DATA, "r") as f:
    log = f.read()

log = log.split("\n")

json = {
    "gesamt": 0,
    "nach_level": {"INFO": 0, "ERROR": 0, "WARNING": 0, "CRITICAL": 0},
    "nach_user": {"Max": 0, "Peter": 0, "Laura": 0, "Günther": 0},
    "erster_critical": None
}




for lines in log:
        
        json["gesamt"] += 1
        
        #Definition Message
        info = re.findall("INFO", lines)
        error = re.findall("ERROR", lines)
        warning = re.findall("WARNING", lines)
        critical = re.findall("CRITICAL", lines)

        if bool(info) == True: 
              json["nach_level"]["INFO"] += 1
        elif bool(error) == True:
              json["nach_level"]["ERROR"] += 1
        elif bool(warning) == True:
              json["nach_level"]["WARNING"] += 1
        elif bool(critical) == True:
              json["nach_level"]["CRITICAL"] += 1
        
              
        #Definition Namen
        Max = re.findall("Max", lines)
        Laura = re.findall("Laura", lines)
        Peter = re.findall("Peter", lines)
        Günther = re.findall("Günther", lines)


        if bool(Max) == True: 
              json["nach_user"]["Max"] += 1
        elif bool(Laura) == True:
              json["nach_user"]["Laura"] += 1
        elif bool(Peter) == True:
              json["nach_user"]["Peter"] += 1
        elif bool(Günther) == True:
              json["nach_user"]["Günther"] += 1
        
              




        print(bool(info))



    #print(lines)



print(json)



