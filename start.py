print("Hello world")

if 5 > 2:
    print("5 is greater")
    print("2 is smaller")

x = 5
y = "Hello World"
print(id(x))
print(id(y)) # gives memory id of variable
print(type(x))
print(type(y)) 
# Python class note.
mail = """Multi 
line
string"""
print (mail)

d= 7.5
print(type(d))

e = int(d)
print(type(e))

a = 3
b = "2"

if a > int(b):
    print("a is greater")


a = 1
A = 4

age = 8
Age = 10 #different variables

myObject = 5 # Camel Case
MyObject = 5 # Pascal Case
my_object = 5 # Snake Case

x,y,z = "Orange", "Banana", "Mango"
print(x)
print(y)
print(z)



a = True
b = False
print(a and b)
print(a or b)
print(not b)


boy_age = 19
boy_country = "Nepal"

if boy_age > 18 and boy_country == "Nepal":
    print("Boy can give licence exam in nepal")


first_number = float(input("Enter your first number : "))
second_number = float(input("Enter your second number : "))

# first_number = int(first_number)
print("Addition = ", first_number + second_number)

first_number = float(input("Enter your first number : "))
second_number = float(input("Enter your second number : "))
print("Subtraction = ", first_number - second_number)

first_number = float(input("Enter your first number : "))
second_number = float(input("Enter your second number : "))
print("Multiplication = ", first_number * second_number)

first_number = float(input("Enter your first number : "))
second_number = float(input("Enter your second number : "))
print("Division = ", first_number / second_number)

for x in "banana":
  print(x) 

a = "Hello, World!"
print("Length ===", len(a))

txt = "The best things in life are free!"
print("free" in txt)

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-2:-5])
b = "Hello, World!"
print(b[:-5])

b = "Hello, World!"
print(b.upper())
print(b.lower())
print(b.capitalize())

b = " Hello  "
print(b.strip())

b = "Hello, World!"
print(b.replace("World", "Ishani"))

z = b.split(",")
print(z)

name = input("Enter your name")

print("You have entered your name = " + name )
print(f"You have entered your name = {name}")
print("You have entered your name = %s" % (name)) 