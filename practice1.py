batteries = [50, 30, 4, 45, 12, 18, 30] ## battery basket 

minimum_battery_power = 20          ## battery use minimum 20% charge

usable_battery_power = 0     ##battery 0 means power also 0
usable_battery_count = 0     ## usable battery 0
for battery in batteries:    ## check every battery
    if battery > minimum_battery_power:           # check if battery is over charge 20% to use
        usable_battery_power += battery   #if yes use power added
        usable_battery_count = usable_battery_count + 1     # if yes use battery count add
print(f"There are {usable_battery_count} batteries which can be used to generate {usable_battery_power} power ")



### next # challenge 2: alien message decoder
alien_message = "neila na ma I. uoy era woh namuh ih"
print(f"""
Alien message = {alien_message}
Now, Human message = {alien_message[::-1]}  
""") ## reverse string


### challenge 3: resource allocation
available_foods = [
    "apple",
    "banana",
    "Watermelon",
    "chocolate",
    "papaya",
    "grapes",
    "cherry",
    "cupcakes",
    "pizza",
    "burger",
    "cheesecake",
    "bread",
]
available_crews = 3
each_crew_food = len(available_foods) // available_crews
remaining_food_count = len(available_foods) % available_crews
print(f"Each crew get {each_crew_food} food and remaining food count = {remaining_food_count}")


def alien_attack_game():
    print("Welcome to Alien attack Game")
    print("Starting mission........")
    print("Mission completed")

alien_attack_game()


def sum(*args):
    result = 0
    for number in args:
        result += number
    return result

def diff(a,b):
    return a-b 
def mul(a,b):
    return a*b 
def div(a,b):
    return a/b 

print(sum(1,2,3,4,5))


def mul(*args):
    result = 0
    for number in args:
        result *= number
    return result

def diff(a,b):
    return a-b 
def mul(a,b):
    return a*b 
def div(a,b):
    return a/b 
def exponential():
    pass
def print_name(name="Ishani"):
    print(f"Hello {name}")

print(mul(4,5))
print_name()
print_name("Alisha")


def print_full_name(**kwargs):
    print(kwargs)
    print(f"My full name is {kwargs["first_name"]} {kwargs["last_name"]}")
print_full_name(first_name="Ishani", last_name="Giri", middle_name="None")


def print_result(*args, **kwargs):
    print(args)
    print(kwargs)
    result = 0
    for number in args:
        result += number
    print(f"My full name is {kwargs["first_name"]} {kwargs["last_name"]} and total marks = {result}")
print_result(10,20,30,40,50, first_name="Ishani", last_name="Giri")