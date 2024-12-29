def setup_mission(): 
    print("Setting up for the mission.....")
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
    available_crews = int(input("Enter available crews"))
    print("Setup Completed.....") 
    return available_crews, available_foods


# check battries over hundred
def get_charged_battries():
    batteries = [50,30,4, 45, 12, 18, 30]
    minimum_battery_power = 20
    usable_battery_power = 0
    usable_battery_count = 0
    for battery in batteries: 
        if battery > minimum_battery_power:
            usable_battery_power += battery
            usable_battery_count = usable_battery_count + 1
            if usable_battery_power >= 100:
                return usable_battery_power, usable_battery_count

def decrypt_alien_message(alien_message):
    human_message = alien_message[::-1]
    return human_message
def food_divide_equally(foods,crews_member):
    equally_foods = len(foods) //crews_member
    remaining_foods = len(foods) % crews_member
    return equally_foods, remaining_foods

def alien_attack_game():
    print("Welcome to Alien Attack Game")
    print("Starting mission.....")
    setup_mission()
    crews_number, foods = setup_mission()
    print(f"You have {crews_number} astronuts and food available = {foods}")

    print("WELCOME TO THE MARS!!!!!")
    print("Your battery is dead please change the battery")
    battery_power, battery_count = get_charged_battries()
    print("Hurray!!! Your battery is charged.")

    print("Opps... Alien has arrived saying:")
    print("rednerrus")
    decrypted_text = decrypt_alien_message("rednerrus")
    print(f"Alien is saying: {decrypted_text}")
    print("Alien has captured all astronauts")
    print("if astronaut wants to escape they have divide each food and give remaining foods")

    equally_divided, remaining_food = food_divide_equally(foods, crews_number)
    print(f"you have {equally_divided} foods divided equally and remaining = {remaining_food}")
    print("okay... Now you can go to Earth")
    print("Mission Completed")
alien_attack_game()


    