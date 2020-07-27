#here comprehension means writing multilines of code into a single line.
nums=range(50,101)
halfs=[]
for i in nums:
    halfs.append(i/2)
print(halfs)

#or viceversa
halfs=[i/2 for i in range(50,150)]