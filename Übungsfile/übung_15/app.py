import re
import sys
import argparse 


parser = argparse.ArgumentParser(description="gibt Variablen in das System weiter")

parser.add_argument("--path", type=str, help="der Pfad zur Logdatei")

parser.add_argument("--level", type=str, help="Auswahl der Loglevel", choices=["INFO", "WARNING", "ERROR"])

parser.add_argument("--strict",action="store_true")

args = parser.parse_args()  


print(args.path)
print(args.strict)
#Variablen 
if args.path != None:
    file = args.path
else:
    file = "app.log"


#Funktionen 
def file_opener(file):
    try:
        with open(file, "r") as f:
            x = f.readlines()
            return x
    except FileNotFoundError as e:
        print(f"file wurde nicht gefunden : {e}")
        print(f"Haben Sie vielleicht den falschen Pfad angegeben ? : '{file}'")
        sys.exit(1)
    
    


lines = file_opener(file)
dic = {"INFO": 0, "WARNING": 0, "ERROR": 0}

def info_counter(dic, lines = file_opener(file)):
    for line in lines:
        print(line)
        if re.search("INFO", line):
            dic["INFO"] += 1 
        elif re.search("WARNING", line):
            dic["WARNING"] += 1 
        elif re.search("ERROR", line):
            dic["ERROR"] += 1 
            if args.strict == True:
                    if dic["ERROR"] > 1:
                        print("Knie nieder, du Schwein!")
                        sys.exit(1)
            # sys.exit(0 geht hier nicht muss ich umbauen)
        



    return dic





if  __name__ == "__main__":
    print(info_counter(dic))


