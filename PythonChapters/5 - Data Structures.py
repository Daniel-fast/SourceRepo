5 - DATA STRUCTURES




=============================== 8 - Lambda Function   =============================== 

def make_incrementor(b):
    return lambda x: x + b


f = make_incrementor(0)
print()
for c in range(1, 100, 2):
    print(f(c))
print()


(Definir - esta usando Lambda Function)
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(1)
print(f(0))
print(f(1))
print(f(2))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')




=============================== 9 - Map Function   =============================== 

# Map Expression
items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12),
    ("Product 4", 16),
]

#Here we are using a for loop to iterate over the items in the list
prices =[]
for item in items:
    prices.append(item[0]) #The indice of item correspond a list of items: 0 = product and 1 = prices
    
print(prices)


#Here we are using lambda expression and a map expression to iterate over the prices
x = map(lambda item: item[1], items)
print(x) #This way we got a map object (<map object at 0x000001E5AA55ABC0>) that is iterable, so we are going to use a for loop to iterate over the prices

for item in x:
    print(item) #This way we got all the prices - one in each line   10
                                                                    # 9
                                                                    # 12
                                                                    # 16


# We can also transformate the map ina a list - so the for loop is not necessary anymore
prices = list(map(lambda valor: valor[1], items)) 
print(prices) #Ok, here it is [10, 9, 12, 16]



# (x*y for x in range(10) for y in range(x, x+10))   (PESQUISAR RESULTADO)
    
=============================== 15 - Tuples   =============================== 

# Tuple
point = (1, 2, 3)
print(point[0:2])
x, y, z = point
print(point)
print(x)
print(y)
print(z)



=============================== 16 - Swaping variables   =============================== 

x, y = y, x  # with this notation is possible to swap the value of variables without the use of a third variable
# Accuatly we are defining a Tuple (it's possible doing that withou the parentesis)


a = 10
b = 20
c = 30


a, b, c = 1, 2, 3  # it's possible set up values for lots of variables

print("a =", a)
print("b =", b)
print("c =", c)


print("x =", x)
print("y =", y)




=============================== 17 - Arrays   ===============================
# We use arrays for large amout of data (above 10.000 registers) - it's very usefull for it.

# we have a module called array and in this module we have a class called array
from sys import getsizeof
from tomlkit import value
from array import array
x = 10
y = 20


# the first argument is the typecode - in this case, "i" means integer
numbers = array("i", [1, 2, 3])
# that said, keep in mind that new objects in this array must be the same typecode (in this case, integers)


array.append
numbers.append
numbers.pop
numbers.remove
array.insert
array.pop
array.remove

# we have lots of methods to deal with arrays (mostly very identical to lists)
# Array

from array import array

numbers = array("i", [1, 2, 4])
numbers.append(4)
print(array.typecode)


dup_numbers = [1, 2, 3, 4, 5, 6, 6, 7, 1]
print(dup_numbers)
uniques = set(dup_numbers)
print(uniques)
print('manual')




=============================== 18 - Sets   ===============================
# sets are basically a collection of no duplicates

numbers = [1, 1, 2, 5, 6, 7, 3, 2, 8, 7]

print(numbers)  # [1, 1, 2, 5, 6, 7, 3, 2, 8, 7]


uniques = set(numbers)

print(uniques)  # {1, 2, 3, 5, 6, 7, 8} Look, set uses curly braces




=============================== 19 - Dictonaries  ===============================
# They are a very powerfull way to store keyvalue pairs

point = dict(x=1, y=2, z=4)

# diferent from the lists, we don't have a index to search, instead, we use the key for search
print(point["z"])

point["x"] = 25  # we can change the value of a key

print(point)  # printing give us like a Json {'x': 25, 'y': 2, 'z': 4}

# we can change the value type too - {'x': 25, 'y': 2, 'z': 'love'}
point["z"] = "love"

print(point)

if "z" in point:
    print(point["z"])
else:
    print("Value doesn't exist in the dictonary")

if "k" in point:
    print(point["z"])  # We can check if a dictionary has a value
else:
    print("Value doesn't exist in the dictonary")  # or

print(point.get("x"))  # we can use the get method

print(point.get("k"))  # when a value doesn't exist, "None" is registered

check_value = point.get("k")  # even when using a variable, None is recorded

print(check_value)  # "None"


# we can use an argument of a value to be used in a case the value doesn't exist - this case "0"
print(point.get("k", 0))
print()

for key in point:  # we can iterate to get all the keys
    print(key)

print()

for chave in point:
    # we can also print the valou pair of the dictinary
    print(chave, point[chave])

for key in point.items():
    print(key)  # we can iterate with the items method and get Tuples ('x', 25)
    # ('y', 2)
    # ('z', 'love')

for key, value in point.items():
    # or we can get each separeted value using to variables: x 25
    print(key, value)
    # y 2
    # z love


=============================== 20 - Dictionary Comprehensions  ===============================
we can create a dictionary using a for loop in a traditional way

values = {}
for x in range(5):
    values[x] = x*2

# but, the best way is to use another extructure like below

# we produce this result {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
# we are going to use it to get the size of the generator expression


values = {x: x * 2 for x in range(5)}
print(values)



=============================== 21- Generator Expressions  ===============================
# there are times when we need to work with a huge amount of data (in a creation) but doesn't want use all the memory
# we use generator expressions
# so, like lists we can iterate over them and each iteration generates a new value but instead of armazening in memory, this is
# only create in real time.
values = (x * 2 for x in range(10))
# instead of showing values, we have this message: <generator object <genexpr> at 0x1064e55b0
print(values)

for x in values:
    print(x)
# we have all the results of the generation
# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18

# it's almost the same sintaxe of lists, but here we use parenthesys
values = (x * 2 for x in range(1000000))
# we need only Generetor: 104 bytes for 1000 itens
print("Generetor:", getsizeof(values))


# it's almost the same sintaxe of lists, but here we use parenthesys
values_list = [x * 2 for x in range(1000000)]
print("List:", getsizeof(values_list))

# Generetor: 104 bytes
# List: 8448728 bytes  - this is a huge diference



=============================== 22- Unpacking Operator  ===============================
numbers = [1, 2, 3, 4, 5]
print(numbers)  # we get all data in this format [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5]
print(*numbers)  # but with the "*" unpacking operator - the result is 1 2 3 4 5

values = list(range(5))  # this is a ordinary list
print(values)

# in this example, we unpacked the string hello and put it in the list
values = [*range(5), *"Hello"]
print(values)  # [0, 1, 2, 3, 4, 'H', 'e', 'l', 'l', 'o']

# we can also combine Dictionaries, let's see:
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second}
print(combined)  # {'x': 10, 'y': 2}
