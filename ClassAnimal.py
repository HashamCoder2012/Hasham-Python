from abc import ABC, abstractmethod 
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")
class Snake(Animal):
    def move(self):
        print("I can crawl")
class Lion(Animal):
    def move(self):
        print("I can roar")
class Dog(Animal):
    def move(self):
        print("I can bark")

R=Human()
R.move()
k=Snake()
k.move()
d=Dog()
d.move()
l=Lion()
l.move()
