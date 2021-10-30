print ("Hello World")

# Multiple Assignments
age = 41
myAge, sonsAge, daughtersAge = age, 5, 12

print(myAge, sonsAge, daughtersAge)

# Repeating String with Multipliers
print ("Batman " + ("Na" *20))

# Placeholders ($)
sentence = "%s %s is the best US President"
print(sentence%("Barack", "Obama"))
print("%s %s is the best US President"%("Bill", "Clinton"))

# Lists
shopList = ["Apples", "Oranges", "Bananas", 1]
shopList2 = [1, 2, 3, "Apples"]

print(shopList, shopList2)

# Remove items from list
del shopList[3]
shopList.append("Cheese")
print(shopList)

# List Length
print(len(shopList))

print(max(shopList))
print(min(shopList))

# Dictionaires
capitals = {"RS": "Porto Alegre", "SC": "Floripa", "PR": "Curitiba", "ES": "Vitória"}
del capitals["ES"]

print(capitals)
print(capitals["RS"])

meal = ("Rice", "Beans", "Juice", 5)
print(meal)

# Conditionals
a, b = 5, 44

if (a > b):
    print("Greater")
else:
    print("Smaller")

time = 21
if (time < 12):
    print("G'day")
elif(time > 12 and time < 20):
    print("Afternoon")
else:
    print("Nighty night")

# For Loops
## Iterate over tuple/lists
for item in meal:
    print(item)

## Regular Loop
for i in range(0, 10):
    print(i)

for i in range(0, 11, 2):
    print(i)

for i in range(5, 51, 5):
    print(i)
    print("\n")

#While Loops
c = 0
while c < 5:
    print(c)
    c = c + 1
    if (c == 3):
        break # Continue / Return

# Try/Except
try:
    if name > 3:
        print("Greater")
except:
    print("Issue encountered")
    
# Functions
def Greeter(name):
    print("Hello " + name)
    
def Add(num1, num2):
    return num1 + num2

Greeter("Hiram")
sum = Add(1, 1)
print(sum)

# Built-In Functions
print(abs(-3))
print(bool(0))
print(bool())

# dir: lists all possible operations on an object or function
print("dir(hello)")
print(dir("hello"))

print("dir(print)\n")
print(dir(print))

# Define the builtin 'help'.: This is a wrapper around pydoc.help that provides a helpful message
# help(print)
# help(dir)

cmdSentence = 'print("Hi")'
eval(cmdSentence) # Single Line execution
exec(cmdSentence) # Multi Line execution

# Built-In Converters
a = 1
str(a)
float(a)
int(a)

print(str(a) + " is a number")

# OO in Python

class Person:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def getName(self): # self relates to the "this" keyword in C#
        print("Person Class. Name: " + self.name)
    def getNumber(self):
        print("Person Class. Number: " + str(self.number))

p = Person("Hiram", 41)
print(p)

p.getName()
p.getNumber()