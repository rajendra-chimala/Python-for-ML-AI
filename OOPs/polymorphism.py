class car:
    
    def addition(self,x,y,z=0):
        return x+y+z
    
    
myCar  = car()

print(myCar.addition(10,10))
print(myCar.addition(10,10,30))