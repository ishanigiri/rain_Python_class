empty_list = []
empty_list.append("apple")
empty_list.append("banana")

print(empty_list)

['apple']


empty_list.append("apple") # add to list 
empty_list.append("banana")
empty_list.append("apple")   # add to list 
empty_list.append("banana")
for index, fruit in enumerate(empty_list):
    print(f"Item position: {index} and value: {fruit}")

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
print(fruits[1]) 
(green, yellow, *red) = fruits

print(green, yellow, red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
 
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

fruits = {"apple", "mango", "papaya", "pineapple", "cherry"}
for items in fruits:
    print(items)
fruits.add("apple")
print(fruits)
