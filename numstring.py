class Numstring:

    def __init__(self,value):
        self.value=str(value)

    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self,other):
        if "." in self.value:
            return float(self) + other
        return int(self) + other
    #you cannot add float with int. But can add int with float.
    def __radd__(self,other):
        #radd is reflected add or reverse add. so here we can add float with int and viceversa.
        return self + other
    def __iadd__(self,other):
        #def immutable add
        self.value= self + other
        return self.value
    

result=Numstring(5)
print(int(result))
print(float(result))
print(str(result))