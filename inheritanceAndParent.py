import random 

class Community:
    def __init__(self,name,age,**kwargs):
        self.name=name
        self.age=age
        for key,value in kwargs.items():
            setattr(self,key,value)


class House(Community):
    light=False
    singlebed=True

    def __init__(self,name,age,**kwargs):
        super().__init__(name,age,**kwargs)

    def kitchen(self):
       # light=False
        if self.light==True:
            return "There is sufficient light"
        else:
            return "There is no light"

    def hall(self,lightlevel):
         return self.singlebed and lightlevel==10   