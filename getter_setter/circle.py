class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    #if you want to only access by yourself use @property
    @property
    def diameter(self):
        return self.radius*2
    
    #if you want to set the diameter.
    @diameter.setter
    def radius(self,diameter):
        self.radius=diameter/2
        

"""c=Circle(10)
print(c.diameter())"""