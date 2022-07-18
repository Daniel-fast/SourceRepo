from collections import namedtuple
from abc import ABC, abstractclassmethod
import math
7 - CLASSES
== == == == == == == == == == == == == = 1 - Classes == == == == == == == == == == == == == == ==


class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = math.sqrt(y)
        # self.z = math.pow(z, x)
        # self.u = math.exp(u)
        # self.r = math.pi * math.pow(r, 2)

    def draw(self):
        # print(f"x = {self.x}, y = {self.y}, z = {self.z}, u = {self.u}")
        print(f"x = {self.x}, y = {self.y}")
        print()

    # def area(self):
    #     print(f"Area = {self.r}")
    #     print()


Point.default_color = "Green"
point = Point(6, 9)
print()
print(Point.default_color)
print()
print(point.default_color)
print()

another = Point(7, 81)
point.draw()
print()
another.draw()
print()
print(another.default_color)
print()
print(Point.__annotations__)
# area = Point.area(10)


print(isinstance(point, Point))


== == == == == == == == == == == == == == 5 - Class x Instance Methods == == == == == == == == == == == == == =


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"x = {self.x}, y = {self.y}")
        print()


point = Point.zero()
point.draw()
print(point)

== == == == == == == == == == == == == = 6 - Magic Methods == == == == == == == == == == == == == =

# https://rszalski.github.io/magicmethods/     list all the magic methods


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"x = {self.x}, y = {self.y}")
        print()


point = Point(1, 2)
print(point)
print()
print(str(point))


== == == == == == == == == == == == == = 7 - Comparing Objects == == == == == == == == == == == == == =

# https://rszalski.github.io/magicmethods/     list all the magic methods


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"x = {self.x}, y = {self.y}")
        print()


point = Point(0, 1)
other = Point(1, 2)
print(point < other)


== == == == == == == == == == == == == = 8 - Performing Arithmetic Operations == == == == == == == == == == == == == =

https: // rszalski.github.io/magicmethods / list all the magic methods


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"x = {self.x}, y = {self.y}")
        print()


point = Point(10, 1)
other = Point(5, 2)
print(point.x + other.x)


== == == == == == == == == == == == == = 9 - Making Custom Containers == == == == == == == == == == == == == =


class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")

print(cloud.tags)


# == == == == == == == == == == == == == = 10 - Private Members == == == == == == == == == == == == == == ==


# class TagCloud:
#     def __init__(self):
#         self.tags = {}

#     def add(self, tag):
#         self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return (self.tags.get(tag.lower(), 0))

#     def __setitem__(self, tag, count):
#         self.tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.tags)

#     def __iter__(self):
#         return iter(self.tags)


# cloud = TagCloud()


# cloud.add("python")
# cloud.add("python")
# cloud.add("python")
# cloud.add("Python")
# cloud.add("chuva")
# cloud.add("Chuva")

# print(cloud.tags)
print()
# executing this line of code returns this result: 4 (assuming that we have 4 keys in the dictionary)
print(cloud["PYTHON"])
print()


# However, if we try to se the dictorary itsef, like this below:
# print(cloud.tags["PYTHON"])
# we will receive this error
# Traceback (most recent call last):
#   File "/Users/danielnascimento/Documents/GitHub/source/Python/app/app.py", line 43, in <module>
#     print(cloud.tags["PYTHON"])
# KeyError: 'PYTHON'

# because we don't really have upper cases "PYTHON" in the dictonary, so
# it's important to "Hide" this method: cloud.tags
# and we do it putting the cursor over the method, pressing F2 and adding "__"before the method


class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return (self.__tags.get(tag.lower(), 0))

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


# cloud = TagCloud()

# cloud.add("python")
# cloud.add("python")
# cloud.add("python")
# cloud.add("Python")
# cloud.add("chuva")
# cloud.add("Chuva")

# # print(cloud.tags)
# print()
# # executing this line of code returns this result: 4 (assuming that we have 4 keys in the dictionary)
# # print(cloud["PYTHON"])
# print()


# this way, we change alls the value of methods like that:  self.__tags = {}

# if we try to access this method, this is going to bem hidden (cloud.tags)

# ok, swe have the: __tags attribute but, if we try to run we get another error:

# print(cloud.__tags)

# AttributeError: 'TagCloud' object has no attribute '__tags' (an Attribute error)
# it's a simple way to say: Hey, don't touch that, it's hidden.
# We have a way to access all the attributes a class have:


cloud = TagCloud()
print(cloud.__dict__)

# it will return: {'_TagCloud__tags': {}}
# so, we get the attribute: _TagCloud__tags and we can use that, let me show that:

print(cloud._TagCloud__tags)  # we get this result: {}

# so, in Python, unlike languages like C# or Java, we don't really have the concept of private members.
# this private members are still accessible from the outside.
# using double underscore is more a convention to prevent accidental access to these "private" members.


# == == == == == == == == == == == == == = 11- Properties == == == == == == == == == == == == == == ==

#
# class Product:
#     def __init__(self, price):
#         self.set_price(price)

#     def get_price(self):
#         return self.__price

#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be less or igual to zero")
#         self.__price = value

#     def valor(self):
#         print(f"US$ {self.__price}")
#         print()

class Product:
    def __init__(self, price):
        self.set_price(price)
        # return print(f"$ {self.price},00")

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Value cannot be 0 or negative")
        self.__price = value

    price = property(get_price, set_price)


product = Product(25)
# product this way, the class Product has too many methods -  get_price, set_price and price and it makes us confused

# print(product.get_price)

# print(product.price)

# product.valor()

# a better way is using properties - like below (this class is igual to Product and has the porpuse to show)

# Like the example in class Product
# class Project:
#     def __init__(self, duration):
#         self.set_duration(duration)
#         # return print(f"$ {self.duration},00")

#     def get_duration(self):
#         return self.__duration

#     def set_duration(self, value):
#         if value < 0:
#             raise ValueError("Value cannot be 0 or negative")
#         self.__duration = value

#     duration = property(get_duration, set_duration)


# Now using Properties trought declarators. Earlier we used a declarator to converts a instance method to a class method

class Project:
    def __init__(self, duration):
        # we need to change the CONSTRUCTOR  because we don't need to use "__duration"
        self.duration = duration

    @property  # Now we are going to use a "Property" DECLARATOR to this method
    def duration(self):  # when the Python interpreter sees this code, he automatically creates a property object called "duration"
        return self.__duration

    # similarly, we need to apply a DECLARATOR to this method,
    # the name of the declarator starts with the name of the property "duration" .setter
    @duration.setter
    def duration(self, value):
        if value < 0:
            raise ValueError("Value cannot be 0 or negative")
        self.__duration = value


# if we try a negative value, we got thrown an exeption: "raise ValueError("Value cannot be 0 or negative")
project = Project(-30)
# ValueError: Value cannot be 0 or negative'

project = Project(30)
print(project.duration)  # shows 30 (and have only one method)

### Beatiful ####


# == == == == == == == == == == == == == = 12- Inheritance == == == == == == == == == == == == == == ==

class Mammal:
    def eat(self):
        print("eat")

    def walf(self):
        print("walk")

# Note of agility: Select the lines of code and then press Shift + alt + down arrow    and the code will be copied down


class Fish:
    # Look, it's the same method of Mammal class, so we can use inheritance.
    def eat(self):
        print("eat")

    def swim(self):
        print("swim")

# DRY (Don't Repeat Yourself)


# USING INHERITANCE ======

# lets creat a class called Animal

class Animal:
    def eat(self):
        print("eat")

# and create the class Mammal


# Animal: Parent, base
# Mammals: Child, Sub-class


class Mammals(Animal):
    def walf(self):
        print("walk")

# Animal: Parent, base
# Fishes: Child, Sub-class


class Fishes(Animal):
    def swim(self):
        print("swim")


m = Mammals()
m.eat()
# wen we create an object from the class we can see it has this methods.
m.walf()

f = Fishes()
f.eat()
f.swim()  # the same occurs when dealing with the Fishes class


# when we run this program, we got:
# eat
# walk
# eat
# swim

# The same happens to CONSTRUCTORS.

class Vehicle:
    def __init__(self):
        self.velocity = 80

    def road(self):
        print("road")


class Car(Vehicle):
    def airbag(self):
        print("airbags")


class Bike(Vehicle):
    def handlebar(self):
        print("handlebar")


c = Car()
c.airbag()
# print(c.velocity)
# Run
#   airbags
#   80


# == == == == == == == == == == == == == = 13- The Object Class == == == == == == == == == == == == == == ==

class Vehicle:
    def __init__(self):
        self.velocity = 80

    def road(self):
        print("road")


class Car(Vehicle):
    def airbag(self):
        print("airbags")


class Bike(Vehicle):
    def handlebar(self):
        print("handlebar")


c = Car()
c.airbag()


print(isinstance(c, Car))  # True because c is an instance of the class Car
# True but, as Car inherits from Vehicle, c is also an instance of Vehicle
print(isinstance(c, Vehicle))


print(isinstance(c, object))
# (footnote) True - also true because all classes inherits from "object"

# We have another built in function:
print(issubclass(Car, Vehicle))
# True because Car is also a subclass of Vehicle


# == == == == == == == == == == == == == = 14- Method Overriding == == == == == == == == == == == == == == ==

# We have two classes beig Car a derivation of Vehicle
class Vehicle:
    def __init__(self):
        self.velocity = 80

    def road(self):
        print("road")


class Car(Vehicle):
    def airbag(self):
        print("airbags")

# suppose we want use other CONSTRUCTOR to Car - like: power - let's See


class Vehicle:
    def __init__(self):
        self.velocity = 80

    def road(self):
        print("road")


class Car(Vehicle):
    def __init__(self):
        self.power = 400

    def airbag(self):
        print("airbags")


c = Car()

print(c.velocity, c.power)
# we got this error: AttributeError: 'Car' object has no attribute 'velocity'
# it happens because the __init__ CONSTRUCTOR of Car "OVERRIDES" the __init__ of Vehicle

# to avoid that we use: super


class Vehicle:
    def __init__(self):
        self.velocity = 80

    def road(self):
        print("road")


class Car(Vehicle):
    def __init__(self):
        # this function "super()" can be used for other methods of the parent class
        super().__init__()
        self.power = 400

    def airbag(self):
        print("airbags")


c = Car()
print(c.velocity, c.power)  # Now we got: 80 400

# Lets get some fun


class Vehicle:
    def __init__(self):
        print("Vehicle contructor")
        self.velocity = 80

    def road(self):
        print("road")


class Car(Vehicle):
    def __init__(self):
        # this function "super()" can be used for other methods of the parent class
        super().__init__()
        print("Car contructor")
        self.power = 400

    def airbag(self):
        print("airbags")


c = Car()
print(c.velocity)
print(c.power)

# run

# Vehicle contructor
# Car contructor
# 80
# 400


# == == == == == == == == == == == == == = 17- A Good Example of Inheritance == == == == == == == == == == == ==

class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network.")


# == == == == == == == == == == == == ==  18- Abstract Base Classes == == == == == == == == == == == ==
# (from abc whose stands for abstract, we will import ABC and the
# abstractclassmethod ) - the name of the module is lower case and the name of the class is Uppercase


class InvalidOperationError(Exception):
    pass


class Stream(ABC):  # the first step to make this Stream class an abstract class, we shoud derive it from the ABC class
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    @abstractclassmethod  # the third step is to use the @abstractclassmethod declarator
    def read(self):  # the second step is to make the read method - this method has no implementation
        pass  # so we simple pass here


class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network.")


# == == == == == == == == == == == == ==  19- Polymorphism  == == == == == == == == == == == ==


class UIControl(ABC):
    @abstractclassmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


class ComboBox(UIControl):
    def draw(self):
        print("ComboBox")


# =========
# this is a function called draw that takes a UI Object(control) and constant draw method o it
def draw(controls):
    for control in controls:
        control.draw()
        control.draw()
# =========


# now we create a DropDownList object  (ddl) and pass it to this draw function like this
ddl = DropDownList()
#print(isinstance(ddl, UIControl))
textbox = TextBox()

combobox = ComboBox()
# it should be fine because the DropDownList is an instance of the UIControl class
draw([ddl, textbox, combobox])


# == == == == == == == == == == == == ==  20- Duck Typing  == == == == == == == == == == == ==


# class UIControl(ABC):
#     @abstractclassmethod
#     def draw(self):
#         pass


# class TextBox(UIControl):
class TextBox:
    def draw(self):
        print("TextBox")


# class DropDownList(UIControl):
class DropDownList:
    def draw(self):
        print("DropDownList")


# class ComboBox(UIControl):
class ComboBox:
    def draw(self):
        print("ComboBox")


# =========
# this is a function called draw that takes a UI Object(control) and constant draw method o it
def draw(controls):
    for control in controls:
        control.draw()
        control.draw()
# =========


# Poymorphysm behavior, or the commom method that we need in this derivative - with this we achieve the polymorphic
# behavior in our draw function.

# But because Python is a Dynamic type language, we dont's necessary need this UI controls as the base class here,
# in other words, if we get rid of this class, let's just comment for now, with this change we also achieve polymorphism behavior

# As we can see in line 33, for Python, independent os the type of object, it can be iterable and Python will be
# happy, that's we called Duck Typing. So if it walks like a duck, and quack like a duck, it's a duck
# That's how Python works - because Python is a dynamic language and it doesn't check the type of object
# it only looks for the existence of certain methods in your projects

ddl = DropDownList()
textbox = TextBox()
combobox = ComboBox()

draw([ddl, textbox, combobox])


# == == == == == == == == == == == == 21- Extending Built-in Types == == == == == == == == == == == ==

class Text(str):  # self represents the objetc that im this example represents an instance of the class
    def dobrar(self):
        return self + self


text = Text("Teste")
print(text.dobrar())


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()

list.append("1")


# == == == == == == == == == == == == 22- Data Classes == == == == == == == == == == == ==

# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y #we need to do this because to campare objects


# p1 = Point(1, 2)
# p2 = Point(1, 2)

# print(p1 == p2)

# print(id(p1))
# print(id(p2))

# but the best way is to use a main couple instance:


Point = namedtuple("Point", ["x", "y"])

p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)

print(p1.x)

print(p1 == p2)
