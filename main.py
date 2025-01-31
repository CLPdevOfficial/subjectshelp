import os
import math
import sys
from pyfiglet import Figlet

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title(text):
    figlet = Figlet(font="slant")
    print(f"\033[92m{figlet.renderText(text)}\033[0m")

def get_input(prompt):
    user_input = input(prompt).strip().lower()
    if user_input == "x":
        print("\nExiting the program...")
        sys.exit(0)
    return user_input

def get_float_input(prompt):
    while True:
        try:
            return float(get_input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

# ------------------- Mathematics Formulas -------------------

def area_of_triangle():
    print("Formula: A = (base * height) / 2")
    base = get_float_input("Enter base: ")
    height = get_float_input("Enter height: ")
    print(f"Area: {0.5 * base * height}")

def area_of_rectangle():
    print("Formula: A = length * width")
    length = get_float_input("Enter length: ")
    width = get_float_input("Enter width: ")
    print(f"Area: {length * width}")

def area_of_circle():
    print("Formula: A = π * r²")
    radius = get_float_input("Enter radius: ")
    print(f"Area: {math.pi * radius**2:.2f}")

def perimeter_of_rectangle():
    print("Formula: P = 2 * (length + width)")
    length = get_float_input("Enter length: ")
    width = get_float_input("Enter width: ")
    print(f"Perimeter: {2 * (length + width)}")

def circumference_of_circle():
    print("Formula: C = 2πr")
    radius = get_float_input("Enter radius: ")
    print(f"Circumference: {2 * math.pi * radius:.2f}")

def volume_of_cube():
    print("Formula: V = side³")
    side = get_float_input("Enter side length: ")
    print(f"Volume: {side ** 3}")

def volume_of_sphere():
    print("Formula: V = (4/3) * π * r³")
    radius = get_float_input("Enter radius: ")
    volume = (4/3) * math.pi * radius**3
    print(f"Volume: {volume:.2f}")

def distance_between_points():
    print("Formula: d = √((x2 - x1)² + (y2 - y1)²)")
    x1 = get_float_input("Enter x1: ")
    y1 = get_float_input("Enter y1: ")
    x2 = get_float_input("Enter x2: ")
    y2 = get_float_input("Enter y2: ")
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"Distance: {distance:.2f}")

def quadratic_formula():
    print("Formula: x = (-b ± √(b² - 4ac)) / 2a")
    a = get_float_input("Enter a: ")
    b = get_float_input("Enter b: ")
    c = get_float_input("Enter c: ")
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"Roots: {x1:.2f}, {x2:.2f}")
    else:
        print("No real roots.")

def slope_of_line():
    print("Formula: m = (y2 - y1) / (x2 - x1)")
    x1 = get_float_input("Enter x1: ")
    y1 = get_float_input("Enter y1: ")
    x2 = get_float_input("Enter x2: ")
    y2 = get_float_input("Enter y2: ")
    if x2 - x1 != 0:
        print(f"Slope: {(y2 - y1) / (x2 - x1):.2f}")
    else:
        print("Slope is undefined.")

def pythagorean_theorem():
    print("Formula: c² = a² + b²")
    a = get_float_input("Enter a: ")
    b = get_float_input("Enter b: ")
    c = math.sqrt(a**2 + b**2)
    print(f"Hypotenuse: {c:.2f}")

# ------------------- Physics Formulas -------------------

def force():
    print("Formula: F = m * a")
    mass = get_float_input("Enter mass (kg): ")
    acceleration = get_float_input("Enter acceleration (m/s²): ")
    print(f"Force: {mass * acceleration} N")

def acceleration():
    print("Formula: a = (v_f - v_i) / t")
    v_i = get_float_input("Enter initial velocity (m/s): ")
    v_f = get_float_input("Enter final velocity (m/s): ")
    time = get_float_input("Enter time (s): ")
    print(f"Acceleration: {(v_f - v_i) / time:.2f} m/s²")

def work():
    print("Formula: W = F * d * cos(θ)")
    force = get_float_input("Enter force (N): ")
    distance = get_float_input("Enter distance (m): ")
    angle = get_float_input("Enter angle (degrees): ")
    work_done = force * distance * math.cos(math.radians(angle))
    print(f"Work: {work_done:.2f} J")

def kinetic_energy():
    print("Formula: KE = (1/2) * m * v²")
    mass = get_float_input("Enter mass (kg): ")
    velocity = get_float_input("Enter velocity (m/s): ")
    ke = 0.5 * mass * velocity**2
    print(f"Kinetic Energy: {ke:.2f} J")

# ------------------- Selection Functions -------------------

def select_math_formula():
    formulas = {
        "1": area_of_triangle,
        "2": area_of_rectangle,
        "3": area_of_circle,
        "4": perimeter_of_rectangle,
        "5": circumference_of_circle,
        "6": volume_of_cube,
        "7": volume_of_sphere,
        "8": distance_between_points,
        "9": quadratic_formula,
        "10": slope_of_line,
        "11": pythagorean_theorem,
    }

    while True:
        print("\nSelect a Math formula (or 'x' to exit):")
        for key, value in formulas.items():
            print(f"[{key}] {value.__name__.replace('_', ' ').title()}")
        choice = get_input("> ")

        if choice in formulas:
            clear_console()
            print_title("Mathematics")
            formulas[choice]()
        else:
            print("Invalid selection. Try again.")

def select_physics_formula():
    formulas = {
        "1": force,
        "2": acceleration,
        "3": work,
        "4": kinetic_energy,
    }

    while True:
        print("\nSelect a Physics formula (or 'x' to exit):")
        for key, value in formulas.items():
            print(f"[{key}] {value.__name__.replace('_', ' ').title()}")
        choice = get_input("> ")

        if choice in formulas:
            clear_console()
            print_title("Physics")
            formulas[choice]()
        else:
            print("Invalid selection. Try again.")

def select_subject():
    while True:
        clear_console()
        print_title("CLPdev.sst")
        print("Select a subject (or 'x' to exit):")
        print("[1] Mathematics")
        print("[2] Physics")
        subject = get_input("> ")

        if subject == "1":
            clear_console()
            print_title("Mathematics")
            select_math_formula()
        elif subject == "2":
            clear_console()
            print_title("Physics")
            select_physics_formula()
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    try:
        select_subject()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        sys.exit(0)
