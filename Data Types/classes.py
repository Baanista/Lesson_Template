
class Animal():
    def __init__(self, noise, location):
        self.noise = noise
        self.location = location

    def hear_noise(self):
        print(self.noise)




class Cow(Animal):
    def __init__(self):
        self.noise = "moo"
        self.location = "Every Where"

    def eat_grass(self):
        print(self.noise, "... I am eating grass")


lion = Animal("rawr", "Africa")
lion.hear_noise()
lion.noise = "meow"
lion.hear_noise()

American_Cow = Cow()
American_Cow.hear_noise()
American_Cow.eat_grass()
print(American_Cow.location)
American_Cow.location = "America"
print(American_Cow.location)