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
# comment
user_choice = input(""" 
            please choose your option
                + for Addition
                - for Subtraction

                    """)
if user_choice == "+":
    print("Addition = ", first_number + second_number)
elif user_choice == "-":
    print("Subtraction = ", first_number - second_number)
else:
    print("Invalid option")

first_number = int(input("Enter your first number : ")) 
user_choice = input(""" 
            please choose your option
                + for Addition
                - for Subtraction
                ^ for double

                    """)
if user_choice == "+":
    print("Addition = ", first_number + second_number)
elif user_choice == "-":
    print("Subtraction = ", first_number - second_number)
elif user_choice == "-":
    print("Power = ", first_number - second_number)
else:
    print("Invalid option")
