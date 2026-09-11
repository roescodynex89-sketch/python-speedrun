class Animal:
    def __init__(self, name, sound):   # constructor
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

# Object তৈরি
dog = Animal("Dog", "Woof")
dog.make_sound()   # Dog says Woof

# Inheritance
class Puppy(Animal):
    def __init__(self, name):
        super().__init__(name, "Yip")   # parent class-এর constructor call
        self.age = 0.5

    def make_sound(self):               # method override
        super().make_sound()            # parent-এর method-ও call করা যায়
        print(f"{self.name} is a puppy, age {self.age}")

p = Puppy("Tommy")
p.make_sound()