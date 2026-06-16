




class Service:
    def __init__(self,name,url,response_time,status_code):
        self.name = name
        self.url=url
        self.response_time=response_time
        self.status_code=status_code
    
    def ist_gesunf(self):
        if self.status_code == 200 and self.response_time < 500: