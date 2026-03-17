from animal import Animal, Dog, Cat

dog1 = Dog("Buddy", 3, 20, "Labrador")
cat1 = Cat("Misty", 2, 5, "White")
animal1 = Animal("Generic", 5, 10)

animals = [dog1, cat1, animal1]

for a in animals:
    print(a)
    print(a.eat())
    print(a.speak())
    print()