class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.energy = 1
        
    def describe(self):
        return f"{self.name} is {self.color} and has {self.energy} energy"
    
    def exercise(self):
        try:
            if self.energy > 0:
                print(f"You take {self.name} for a walk")
                self.energy -= 1
            else:
                raise RuntimeError(f"{self.name} is too tired")
        except RuntimeError as e:
            print(f"Something went wrong: {e}")
        
    def feed(self):
        try:
            if self.energy < 5:
                print(f"You fed {self.name}")
                self.energy += 1
            else:
                raise RuntimeError(f"{self.name} is too tired")
        except RuntimeError as e:
                print(f"Something went wrong: {e}")
        
dog = Dog("Ginger", "brown") # creating instance/object of class 'Dog'
dog1 = Dog("Perichalli", "blue")

print(my_dog.describe())