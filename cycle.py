class Animal:

    def __init__(self, z):
        self.x = 0
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

s = Animal("Erik")
s.party()

j = Animal("Jim")
j.party()
s.party()