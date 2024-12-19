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

def alien_attack_game():
    print("Welcome to Alien Attack Game")
    print("Starting mission.....")
    setup_mission()
    crews_number, foods = setup_mission()
    print(f"You have {crews_number} astronuts and food available = {foods}")

    print("WELCOME TO THE MARS!!!!!")
    print("Your battery is dead please change the battery")

    print("Mission completed")

alien_attack_game()

