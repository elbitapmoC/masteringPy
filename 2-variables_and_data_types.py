# There's no comand for delcaring variables.
# one = 1;
# two = 2;
# print(one+two);

# COMMENTS  --------------------------------------------------------------------

# Single Line Comment.

# Multiple
# Line
# Comments

# OR...
"""
Python ignores string literals
that are not assigned
to a variable.
"""
# ------------------------------------------------------------------



# VARIABLE  --------------------------------------------------------------------

# You can use "" or '' to define a string.
# test1 = 1
# TEST1 = 'one'
# print(test1)
# print(TEST1)
# These won't overwrite b/c python is case-sensitive

# You can assign multiple values to multiple variables.
multiVal_a, multiVal_b, multiVal_c = 1, 2, 3
print(multiVal_a)
print(multiVal_b)
print(multiVal_c)

# OR
singleAssign_1 = singleAssign_2 = singleAssign_3 = '🍑'

print(singleAssign_3)
print(singleAssign_2)
print(singleAssign_1)

# Similar to JS, you can destructure from a list (object)
fruits = ['🍎', '🍌', '🍇']
apple, nana, grape = fruits

# OUTPUT VARIABLES...
print(apple,nana,grape) # 🍎 🍌 🍇
# ^ Use this method 
print(apple + nana + grape) # 🍎🍌🍇

# GLOBALS
# You can use the global keyword to modify a global variable from within a function.
x = "👍"

def funcTestA():
  x = "🙌"
  print("Python is " + x);

funcTestA()
def funcTestB():
  global x
  x = "🍯"

funcTestB()

print("Python is " + x);
# ----------------------------------------------------------







# DATA TYPES--------------------------------------------------------
# Text - str
# Numeric - int, float, complex
  # complex - number and 
# Boolean - bool
# Sequence - list, tuple, range
  # range - range(start, stop, step)
  # default step is 1.
  # no need to add it if it's 1.
print(* #unpack operator
      [i for i in range(0, 8) if i > 5], # like arrays in JS, we map through ea value inside the list.
      sep="\n" # sep="\n" is the separator.
)
# Mapping - (dict)ionary - key:value pairs
  # set - stores only unique values
  # frozenset - can not be changed
# Creating a set
fruits = {"🍏", "🍒", '🥭', '🥝'} 
fruits.add('🍓')
fruits.add('🥭')
print(fruits)

# list - list of ordered items (mutable)
# tuple - list of ordered items (immutable)
list_1 = ['🍎', '🍌', '🍇']
tuple_1 = ('🍎', '🍌', '🍇')
range_1 = range(6)

def funcTypeTests(a, b, c):
  return f"{a}\n{b}\n{c}"
print(funcTypeTests(list_1, tuple_1, range_1))

# RANDOM NUMBER
import random
print(random.randint(1, 10))

# TYPE CASTING
floatedType = 1.2345
convertedIntType = int(floatedType)
print(convertedIntType)

# STRINGS-METHODS-START --------
# Targeting individual letters
strTestHelloWorld = "Hello, World!"
print(strTestHelloWorld[0]) # H

strTestHello = "Hello!"
# LOOP THROUGH STRINGS
for i in strTestHello:
  print(i)
print(len(strTestHello))

# String Check (not case sensitive)
stringToCheck = "Don't forget to buy 🍫 CHOCOLATE Milk."
print("Milk" in stringToCheck) # True
if("Vanilla" not in stringToCheck): # True
  print("Vanilla is not on the menu.")

# Slice strings..
print(strTestHelloWorld[0:3]) # Hel 
# ^ from 0 to 2
print(strTestHelloWorld[::-1]) # !dlroW ,olleH
  # ^ reverses the string

print(strTestHelloWorld[:2]) # Starts @ 1st char, counts 2 from 1st char.
print(strTestHelloWorld[7:]) # Starts @ 4th char, goes until reaches the end.
b = "Hello, World!"
print(b[-5:-2]) #orl
# Negative indexing starts at -1.
# (There's no 0)
# From -5 to -3

# METHODS-END --------

# ------------------------------------------------------------------
