# Main program
print("Choose a check to perform:")
print("1. Check if the number is even or odd")
print("2. Check if the number is prime")
print("3. Check if one number is a multiple of another")

# Input choice from the user
choice = int(input("Enter your choice (1, 2, or 3): "))

if choice == 1:
    # Check even or odd
    number = int(input("Enter a number: "))
    result = check_even_odd(number)
    print(f"The number is {result}.")

elif choice == 2:
    # Check prime
    number = int(input("Enter a number: "))
    result = check_prime(number)
    print(f"The number is {result}.")

elif choice == 3:
    # Check if one number is a multiple of another
    number = int(input("Enter the first number: "))
    divisor = int(input("Enter the second number (divisor): "))
    result = check_multiple(number, divisor)
    print(result)

else:
    print("Invalid choice! Please enter 1, 2, or 3.")