
from config import *
import random
import json


def dic_safer(dic):
    with open (INPUT, "w") as f:
        json.dump(dic,f,indent=4)


class Service:
    def __init__(self,name,url,response_time,status_code):
        self.name = name
        self.url=url
        self.response_time=response_time
        self.status_code=status_code
    
    def ist_gesund(self):
        if self.status_code == 200 and self.response_time < 500:
            return True
        else:
            return False 
        
    def zu_dict(self):
        dic = {
            "name": self.name,
            "url": self.url,
            "responetime" : self.response_time,
            "status" : self.status_code,
            "gesund": self.ist_gesund()
        }
        return dic
    

i = 0
list_S = []

while i < 10: 
    random_name = random.choice(NAMES)
    url = "www." + random_name + ".com"
    x = random.choice([200, 200, 200, 404, 500])
    resp = random.randint(50,800)
    test = Service(random_name,url,resp,x)
    test.ist_gesund()
    f = test.zu_dict() 
    list_S.append(f) 
    i += 1 

dic_safer(list_S)

