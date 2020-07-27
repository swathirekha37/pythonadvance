#if we have complex code and in order to  reduce the time complexity we use decorator.
#In decorators functions are known as first class citizens.
#func are objects. we can assign 1 func to another func.

#accessing first class functions.
def access(func,a,b):
    return func(a,b)

def add(x,y):
    return x+y

def sub(x,y):
    return x-y
 

print(access(add,4,7))
print(access(sub,7,2))



#closure:
def outer():
    name="swathi"
    def inner():   #here name can be accessed inside this inner function. This is called closure.
        print(name)
    return inner

closure=outer()
closure()
