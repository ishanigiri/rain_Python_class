# Create a tuple named my_tuple with the given elements
my_tuple = (10, 20, 30, 40, 50)

# Access and print the second element of the tuple
print("Second element of the tuple:", my_tuple[1])

# Attempt to change the third element of the tuple to 35 (expect an error)
try:
    my_tuple[2] = 35
except TypeError as i:
    print("Error:", i)

# Print the entire tuple
print("Every tuple:", my_tuple)

