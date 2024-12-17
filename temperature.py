def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def meters_to_kilometers(meters):
    """Convert meters to kilometers."""
    kilometers = meters / 1000
    return kilometers

def feet_to_inches(feet):
    """Convert feet to inches."""
    inches = feet * 12
    return inches
if __name__ == "__main__":
    # Celsius to Fahrenheit
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius)}°F.")

    # Meters to Kilometers
    meters = float(input("Enter distance in meters: "))
    print(f"{meters} meters is equal to {meters_to_kilometers(meters)} kilometers.")

    # Feet to Inches
    feet = float(input("Enter length in feet: "))
    print(f"{feet} feet is equal to {feet_to_inches(feet)} inches.")
