class b:
    def __init__(self):
        print("It's a bird")
    def swim(self):
        print("Faster swimmer")

class parrot(b):
    def __init__(self):
        super().__init__()
    def migrate(self):
        print("Migratary bird")

o=parrot()
o.swim()
o.migrate()