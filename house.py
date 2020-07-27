import random 

class Home:
    
    singlebed=True

    def kitchen(self,light):
       # light=False
        if light==True:
            return "There is sufficient light"
        else:
            return "There is no light"

    def hall(self,lightlevel):
         return self.singlebed and lightlevel==10   