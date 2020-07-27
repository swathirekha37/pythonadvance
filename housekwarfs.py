import random 

class House:
    light=False
    singlebed=True
    
    def __init__(self,name,age=42,**kwargs):
        self.name=name
        self.age=age
        for key,value in kwargs.items():
            setattr(self,key,value)

    def kitchen(self):
       # light=False
        if self.light==True:
            return "There is sufficient light"
        else:
            return "There is no light"

    def hall(self,lightlevel):
         return self.singlebed and lightlevel==10   