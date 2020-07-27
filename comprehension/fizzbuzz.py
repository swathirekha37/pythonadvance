"""for i in range(1,25):
    if i%3 == 0 and i%7 == 0:
        print(i," ","fizzbuzz")
    elif i%3 == 0:
        print(i," ","fizz")
    elif i%7 == 0:
        print(i," ","bizz")"""

print([i for i in range(1,10) if i%3==0 ])


#print table
rows=range(4)
columns=range(4)
print([(x,y) for x in rows for y in columns])
print([(letter,number) for letter in "abcd" for number in range(1,4)])


#using dictionaries
print({letter : number for letter,number in zip('abcdefghijklmnopqrstuvwxyz',range(1,27))})
#fizzbuzz dictionary
nums=range(1,50)
fizzbuzzes={
    "fizz":[n for n in nums if n%3 ==0],
    "buzz":[n for n in nums if n%7 == 0],
    "fizzbuzz":[n for n in nums if n%3==0 and n%7 ==0]
}

print(fizzbuzzes)

#sets: removes duplicates
print({round(x/y) for y in range(1,10) for x in range(2,21)})
fb={ key:set(value) for key,value in fizzbuzzes.items()}
print("set fb values are",fb)