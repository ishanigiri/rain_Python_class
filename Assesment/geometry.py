def rectangle_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Function to calculate the area and perimeter (circumference) of a circle
def circle_area_perimeter(radius):
    pi = 3.141592653589793  # Using a hardcoded value of pi
    area = pi * radius**2
    circumference = 2 * pi * radius
    return area, circumference

# Function to calculate the area and perimeter of a right-angled triangle
def triangle_area_perimeter(base, height):
    area = 0.5 * base * height
    # Perimeter needs the hypotenuse (c) of the triangle, which can be calculated manually
    hypotenuse = (base**2 + height**2)**0.5  # Using exponentiation to calculate square root
    perimeter = base + height + hypotenuse
    return area, perimeter

# Main program
print("Choose a shape to calculate area and perimeter:")
print("1. Rectangle")
print("2. Circle")
print("3. Triangle")

# Input choice from the user
choice = int(input("Enter your choice (1, 2, or 3): "))

if choice == 1:
    # Rectangle calculations
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area, perimeter = rectangle_area_perimeter(length, width)
    print(f"Rectangle Area: {area}")
    print(f"Rectangle Perimeter: {perimeter}")

elif choice == 2:
    # Circle calculations
    radius = float(input("Enter the radius of the circle: "))
    area, perimeter = circle_area_perimeter(radius)
    print(f"Circle Area: {area}")
    print(f"Circle Circumference: {perimeter}")

elif choice == 3:
    # Triangle calculations
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area, perimeter = triangle_area_perimeter(base, height)
    print(f"Triangle Area: {area}")
    print(f"Triangle Perimeter: {perimeter}")


else:
    print("Invalid choice! Please choose 1, 2, or 3.")
    