def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time, compounds_per_year):
    return principal * (1 + rate / (100 * compounds_per_year))**(compounds_per_year * time) - principal

def main():
    print("Welcome to the Interest Calculator!")
    print("1. Simple Interest")
    print("2. Compound Interest")

    choice = input("Choose the type of interest calculation (1 or 2): ")

    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate (in %): "))
        time = float(input("Enter the time period (in years): "))

        if choice == '1':
            simple_interest = calculate_simple_interest(principal, rate, time)
            print(f"Simple Interest: {simple_interest:.2f}")
        elif choice == '2':
            compounds_per_year = int(input("Enter the number of times interest is compounded per year: "))
            compound_interest = calculate_compound_interest(principal, rate, time, compounds_per_year)
            print(f"Compound Interest: {compound_interest:.2f}")
        else:
            print("Invalid choice! Please choose either 1 or 2.")
    except ValueError:
        print("Invalid input! Please enter numeric values for the inputs.")

if __name__ == "__main__":
    main()
