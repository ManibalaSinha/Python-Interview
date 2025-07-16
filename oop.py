class Person:
   def __init__(self, name):
      self.__name=name
   def get_name(self):
      return self.__name
   def set_name(self, name):
      self.__name=name

from abc import ABC, abstractmethod
class Animal(ABC):
   @abstractmethod
   def speak(self):
      pass
class Dog(Animal):
   def speak(self):
      return "Woof!"
class Animal:
   def speak(self):
      return "Some sound"
class Dog(Animal):
   def speak(self):
      return "Woof"
class Cat:
   def speak(self):
      return "Meow"
class Dog:
   def speak(self):
      return "Woof"
def make_sound(animal):
   print(animal.speak())
make_sound(Cat())
make_sound(Dog())