class v:
    def __init__(self):
        print("Its a parent class")


class bus(v):
    def __init__(self):
        v.__init__('bus')


print(issubclass(bus,v))
print(issubclass(v,bus))
print(issubclass(bus,bus))