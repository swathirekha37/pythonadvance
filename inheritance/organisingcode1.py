class House:
    park=True
    def __init__(self,name,landacres,**kwargs):
        self.name=name
        self.landacres=landacres
        for key,value in kwargs.items():
            setattr(self,key,value)

    def bedrooms(self,NumBedrooms):
        if NumBedrooms==1:
            return "This is single bedroom house."
        else:
            return "This is multibedroom house."

class Office:
    parking=True
    def __init__(self,NumofEmp,AvgSalary):
        self.NumofEmp=NumofEmp
        self.AvgSalary=AvgSalary
    def BigorSmall(self):
        if self.NumofEmp >= 500:
            return "This is an company."
        else:
            return "This is a office."