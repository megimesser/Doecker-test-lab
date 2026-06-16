
from config import *
import random


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
            self.name : "",
            self.url : "",
            self.response_time : 0,
            self.status_code : 0,
            "gesund": self.ist_gesund()
        }
        return dic
    


random_name = random.choice(NAMES)

url = "www." + random_name + ".com"
x = random.choice([200, 200, 200, 404, 500])

print(x)
print(random_name)
print(url)


i = 0
while i < 10: 
    

