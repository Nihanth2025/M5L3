class V:
    def __init__(self,name,speed,mileage):
        self.name=name
        self.speed=speed
        self.mileage=mileage

class C(V):
    pass

c=C("Benz",150,10)

print(c.name)
print(c.speed)
print(c.mileage)