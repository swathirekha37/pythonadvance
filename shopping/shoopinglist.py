#use help command
#use show command

def helpf():
    print("If you want to quit the app enter, quit.")
    print("If you want to see the entered items, enter show.")
    print("If you want to stop adding items, enter stop.")

def showf():
    for j in itemslist:
        print(j)

def addtolist(itemed):
    itemslist.append(itemed)
    print("{} is added. There are {} items in bag.".format(itemed,len(itemslist)))

itemslist=[]

ans=input("do you want to add items? y/n ")
if ans=='y':
    while True:
        item=input("enter the item name: ")
        if item=='quit' or item=='stop':
            break
        elif item=='help':
            helpf()
            continue
        elif item=='show':
            showf()
            continue
        addtolist(item)
   

print('here is your shopping list')

showf()