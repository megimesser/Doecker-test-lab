import json 
from config import *

with open(INPUT,"r") as f: 
    k = json.load(f)


pythonreport = {
    "gesamt": 0,
    "gesund": 0,
    "ungesund": 0,
    "nach_status": {"200": 0, "404": 0, "500": 0},
    "langsamste": None,
    "ungesunde_services": []
}


def reportmerger(report=pythonreport,file=k):

    langsamstes = None
    hilfsvariable = 0

    report["gesamt"] = report.get("gesamt", 0) + len(file)

    for _ in file: 

        #Health

        if _["gesund"] == True:
            report["gesund"] = report.get("gesund", 0) + 1
        else:
            report["ungesund"] = report.get("ungesund", 0) + 1
            report["ungesunde_services"].append(_["name"])
        

        #Status

        if _["status"] == 200:
            report["nach_status"]["200"] = report["nach_status"].get("200", 0) + 1
        elif _["status"]  == 404:
            report["nach_status"]["404"] = report["nach_status"].get("404", 0) + 1
        elif _["status"] == 500:
            report["nach_status"]["500"] = report["nach_status"].get("500", 0) + 1
        

        #
        if _["responetime"] > hilfsvariable:
            hilfsvariable = _["responetime"]
            langsamstes = _["name"]


    report["langsamste"] = langsamstes
    
        


    

        
    
    return report


print(reportmerger())