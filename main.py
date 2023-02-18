class animal:
    def __init__(self):
        self.animals = 234

class dog:
    def __init__(self):
        super().__init__()
        self.legs = "4"

class cat(dog, animal):
     def print(self):
         print(self.animals)
         print(self.legs)

Greya = cat()
Greya.print()