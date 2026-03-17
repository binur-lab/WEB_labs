class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self):
        return f"{self.name} is eating"

    def speak(self):
        return "Some sound"

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}"


class Dog(Animal):
    def __init__(self, name, age, weight, breed):
        super().__init__(name, age, weight)
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

    def fetch(self):
        return f"{self.name} is fetching a ball"

    def __str__(self):
        return f"Dog - {self.name}, Age: {self.age}, Weight: {self.weight}, Breed: {self.breed}"


class Cat(Animal):
    def __init__(self, name, age, weight, color):
        super().__init__(name, age, weight)
        self.color = color

    def speak(self):
        return f"{self.name} says Meow!"

    def scratch(self):
        return f"{self.name} is scratching"

    def __str__(self):
        return f"Cat - {self.name}, Age: {self.age}, Weight: {self.weight}, Color: {self.color}"