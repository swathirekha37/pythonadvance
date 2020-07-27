#create list and fill it with values.
import copy

class FilledList(list):
    def __init__(self,value,count,*args,**kwargs):
        super().__init__()
        for _ in range(count):
            self.append(copy.copy(value))

fl=FilledList([56,34],5)
print(fl)
fl[1]=38
print(fl)