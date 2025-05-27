class person():
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name)
        print(self.id)


class e(person):
    def __init__(self,name,id,s,p):
        self.s=s
        self.p=p
        person.__init__(self,name,id)

o=e("Nihanth",5002,5000000,"Manager")
o.display()