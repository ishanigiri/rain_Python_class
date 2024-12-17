first_number = int(input("Enter your first number : ")) 
user_choice = input(""" 
            please choose your option
                ^ for double
                + for addition
                / for half
                - for Subtraction
                * for Multiplication

                    """)
if user_choice == "+":
    print("Addition = ", first_number +10)
elif user_choice == "-":
    print("Multiplication = ", first_number *2)
elif user_choice == "-":
    print("For double = ", first_number ^2)
elif user_choice == "-":
    print("Division = ", first_number /2)
else:
    print("Invalid option")
    