import random
import sys
import os

print("Hello world")

name = "Austin"
print(name)

print("5 + 2 =", 5 + 2)
print("5 - 2 =", 5 - 2)
print("5 * 2 =", 5 * 2)
print("5 / 2 =", 5 / 2)
print("5 % 2 =", 5 % 2)
print("5 ** 2 =", 5 ** 2)
print("5 // 2 =", 5 // 2)

print("1 + 2 - 3 * 2 =", 1 + 2 - 3 * 2)
print("(1 + 2 - 3) * 2 =", (1 + 2 - 3) * 2)
print('\n * 3')

quote = "\"Always remember, you are awesome!!!"
multi_line_quote = '''Beans is super awesome!!'''
print("%s %s %s" % ('I like the quote', quote, multi_line_quote))

print("I don't like ", end="")
print("newlines")

grocery_list = ['Pizza', 'Coffee', 'Dog food']
print('First Item is', grocery_list[0])

grocery_list[2] = "Cat Food"
print('The new third item is', grocery_list[2])

print(grocery_list[1:3])

other_events = ['Do laundry', 'Pay rent', 'Pick up dog food']

to_do_list = [other_events, grocery_list]
print(to_do_list)

print((to_do_list[1][1]))

grocery_list.append('onions')
print(to_do_list)

grocery_list.remove("onions")
print(to_do_list)

grocery_list.insert(1, "Pickles")
print(to_do_list)

grocery_list.sort()
print(to_do_list)

grocery_list.reverse()
print(to_do_list)

del grocery_list[3]
print(to_do_list)

to_do_list2 = other_events + grocery_list

print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

pi_tuple = (3, 1, 4, 1, 5, 9)

new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

print(len(new_tuple))
print(max(new_tuple))
print(min(new_tuple))

new_tuple.sort()
print(new_tuple)

new_tuple.reverse()
print(new_tuple)

super_villans = {'Fiddler': 'Isaac Bowin',
                 'Captain Cold': 'Leonard Snart',
                 'Weather Wizard': 'Mark Mardon',
                 'Mirror Master': 'Sam Scudder',
                 'Pied Piper': 'Thomas Peterson'}

print(super_villans['Captain Cold'])

del super_villans['Fiddler']

super_villans['Pied Piper'] = 'Hartley Rathway'

print(len(super_villans))

print(super_villans.get("Pied Piper"))

print(super_villans.keys())

print(super_villans.values())

age = 40

# Conditionals

# If / Else Loops

if age > 16:
    print('You are old enough to drive')
else:
    print('You are not old enough to drive')

if age >= 21:
    print('You are old enough to drive a tractor trailer')
elif age >= 16:
    print('You are old enough to drive a car')
else:
    print("You are not old enough to drive")

# Logical operators and, or, not

if (age >= 1) and (age <= 18):
    print("You get a birthday")
elif (age == 21) or (age >= 65):
    print("You get a birthday")
elif not (age == 30):
    print("You don't get a birthday")
else:
    print("You get a birthday party!")

# Looping

# For loop - perform something 10 times
for x in range(0, 10):
    print(x, ' ', end="")

# Print a new line
print('\n')

# For loops to cycle through a list
grocery_list = ['Pizza', 'Coffee', 'Dog food']

for y in grocery_list:
    print(y)

# Define a list of numbers to cycle through
for x in [2, 4, 6, 8, 10]:
    print(x)

# Double up For Loops to cycle through a list
# Lists of lists
num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])

# While Loops
random_num = random.randrange(0, 25)
# Above will generate random number 1-99

while random_num != 15:
    print(random_num)
    random_num = random.randrange(0, 25)

# While Loops with an iterator

i = 0;

while i <= 20:
    if i % 2 == 0:
        print(i)
    elif i == 9:
        break
    else:
        i += 1  # i = i + 1
        continue
    i += 1


# Functions

def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum


print(addNumber(1, 4))
print('What is your name?')

name = sys.stdin.readline()

print('Hello', name)

long_string = "I'll catch you if you fall. The Floor"

print(long_string[0:4])
print(long_string[-5:])
print(long_string[:-5])
print(long_string[:4] + " be there")

print("%c is my %s letter and my number %d number is %.5f" %
      ('X', 'favorite', 1, .14))

# Capitalize the first letter of a string
print(long_string.capitalize())

# Return the index value of the start of a string
print(long_string.find("Floor"))

# Return true if all of the characters are letters
print(long_string.isalpha())

# Length of a string
print(len(long_string))

# Replace one word with another
print(long_string.replace("Floor", "Ground"))

# Strip whitespace
print(long_string.strip())

# Split a string into a list
quote_list = long_string.split(" ")
print(quote_list)

# FileIO
# Create as well as open a file / wb = write to file
test_file = open("test.txt", "wb")
# file mode =
print(test_file.mode)
# File name?
print(test_file.name)
# Write to a file
test_file.write(bytes("Write me to the file\n", 'UTF-8'))

# Close a file
test_file.close()


# Read info from a file after opening
# test_file = open("test.txt", "r+")

# text_in_file = test_file.read()
# print(text_in_file)

# Delete a file
# os.remove("test.txt")

# OBJECTS (Object Oriented Programming)
# Define attributes using variables inside of classes
# The abilities are functions

# CLASSES AND OBJECTS -------------
# The concept of OOP allows us to model real world things using code
# Every object has attributes (color, height, weight) which are object variables
# Every object has abilities (walk, talk, eat) which are object functions

class Animal:
    # None signifies the lack of a value
    # You can make a variable private by starting it with __
    __name = None
    __height = None
    __weight = None
    __sound = None

    # The constructor is called to set up or initialize an object
    # self allows an object to refer to itself inside of the class
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def set_height(self, height):
        self.__height = height

    def set_weight(self, weight):
        self.__weight = weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_name(self):
        return self.__name

    def get_height(self):
        return str(self.__height)

    def get_weight(self):
        return str(self.__weight)

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(self.__name, self.__height, self.__weight,
                                                                      self.__sound)


# How to create a Animal object
cat = Animal('Whiskers', 33, 10, 'Meow')

print(cat.toString())

# You can't access this value directly because it is private
# print(cat.__name)

# INHERITANCE -------------
# You can inherit all of the variables and methods from another class

class Dog(Animal):
    __owner = None

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        self.__animal_type = None

        # How to call the super class constructor
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    # Overwrite functions in the super class
    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}. His owner is {}".format(self.get_name(),
                                                                                       self.get_height(),
                                                                                       self.get_weight(),
                                                                                       self.get_sound(), self.__owner)

    # You don't have to require attributes to be sent
    # This allows for method overloading
    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound)
        else:
            print(self.get_sound() * how_many)


spot = Dog("Spot", 53, 27, "Ruff", "Derek")

print(spot.toString())


# Polymorphism allows use to refer to objects as their super class
# and the correct functions are called automatically

class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()


test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(spot)

spot.multiple_sounds(4)