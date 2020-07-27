from items import Item
from items import Weapon

class Inventory:
    def __init__(self):
        self.slots=[]
    
    def add(self,item):
        self.slots.append(item)
    
    #count num of items in slots array
    def __len__(self):
        return len(self.slots)

    def __contains__(self,item):
        return item in self.slots

    def __iter__(self):
        yield from self.slots
        #if item not in slots use this
        #yield also can be used and best instead return
    
    
#using item class    
inventory=Inventory()
coin=Item('Coin',"A gold coin")
inventory.add(coin)
print(len(inventory))
print(coin.description)

#using weapon class
print("-----using weapon class-----")
sword=Weapon('Sword','Sharp and Shine',500)
inventory.add(sword)

hammer=Weapon('Ham Burger','Its big cutter',403)
inventory.add(hammer)

for i in inventory:
    print(i.description)