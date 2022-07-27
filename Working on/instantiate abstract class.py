# 
# - A class is called an Abstract class if it contains one or more 
# abstract methods. 
# - An abstract method is a method that is declared
# but contains no implementation. 
# - Abstract classes may not be instantiated, and i
# ts abstract methods must be implemented by its subclasses.
# - a way to define interfaces when other techniques like 
# hasattr() would be clumsy or subtly wrong (for example with magic methods).
# - ABCs introduce virtual subclasses, which are classes that don’t 
# inherit from a class but are still recognized by isinstance() and issubclass() functions.
# - The 'abc' module in Python library provides the infrastructure for defining custom abstract base classes.
# - 'abc' works by marking methods of the base class as abstract.
# - Note the abstract base class may have more than one abstract methods. 
# The child class must implement all of them failing which TypeError will be raised.

import abc
class Shape(metaclass=abc.ABCMeta):
   @abc.abstractmethod
   def area(self):
      pass
class Rectangle(Shape):
   def __init__(self, x,y):
      self.l = x
      self.b=y
   def area(self):
      return self.l*self.b
r = Rectangle(10,20)
print ('area: ',r.area())


# Second Example

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price
    
    def display(self):
            print(f'Title: {self.title}')
            print(f'Author: {self.author}')
            print(f'Price: {self.price}')


title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

# Referencies
# https://www.hackerrank.com/challenges/30-abstract-classes/problem
# https://www.pythontutorial.net/python-oop/python-abstract-class/
# https://www.tutorialspoint.com/abstract-base-classes-in-python-abc#:~:text=A%20class%20is%20called%20an,be%20implemented%20by%20its%20subclasses.