age=22
print(type(age))

breadprice=10.4
print(type(breadprice))

greeting='hello world'
print(greeting)

print(type(greeting))

print('hello'*4)
print('In our house there are {} num of people'.format(9))
print('hey we have {} {} {} colors'.format('red','blue','white'))
print('I have {num} {husbandname} and {dnum} daughters'.format(num=1,husbandname='chiru',dnum=2))

a= [1,2,3,4,5,6]

print(a+[7,9])
print(a*2)

a.append(10)
print(a)

a.extend([11,13])
print(a)

b=[12,32,[54,43],67]
print(b)

b.remove([54,43])#in listinlist you cand remove single element like 54 or 43.
print(b)

print(list('Hello'))
print('rekha'.split())
print('I am swathi rekha chiranjeevi"s wife'.split())
print("red:green:blue".split(':'))

favourites=['apple','icecream','cakes']
print("my faourites are: " + ', '.join(favourites))
print("my faourites are: {}" .format(', '.join(favourites)))

#subscripts
name='swathi'
print(name.index('w'))
nameslist=list(name)
print(nameslist.index('i'))
print(nameslist)

#print(namelist.index('th'))
print(nameslist[4])
print(nameslist)

#del:
del nameslist[5]
print(nameslist)

age=24
if not age>30:
    print("less age") 