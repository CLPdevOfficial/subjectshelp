from pyfiglet import Figlet
import os
import math

text = "CLPdev.sst"
font = "slant"  

figlet = Figlet(font=font)
result = figlet.renderText(text)

color_green = '\033[92m'
reset_color = '\033[0m'

colored_result = color_green + result + reset_color

print(colored_result)
subject = input("Select a subject:\n[1] Math\n[2] Pyshics\n")

if subject == "1":
  os.system('cls' if os.name == 'nt' else 'clear')
  text = "Mathematics"
  font = "slant"  

  figlet = Figlet(font=font)
  result = figlet.renderText(text)

  color_green = '\033[92m'
  reset_color = '\033[0m'

  colored_result = color_green + result + reset_color

  print(colored_result)
  formulam = input("Select a formula:\n[1] Area of a triangle\n[2] Area of a rectangle\n[3] Area of a circle\n[4] Perimeter of a rectangle\n[5] Circumference of a circle\n[6] Volume of a cube\n[7] Volume of a sphere\n[8] Distance between two points\n[9] Quadratic Formula\n[10] Slope of a line\n[11] Pythagorean Theorem\n")
  if formulam == "1":
    text = "Area of a triangle"
    font = "slant"  

    figlet = Figlet(font=font)
    result = figlet.renderText(text)

    color_green = '\033[92m'
    reset_color = '\033[0m'

    colored_result = color_green + result + reset_color

    print(colored_result)
    print("Area of a triangle")
    print("Formula: A = (base * height) / 2")
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("The area of the triangle is:", area)

  elif formulam == "2":
    text = "Area of a rectangle"
    font = "slant"  

    figlet = Figlet(font=font)
    result = figlet.renderText(text)

    color_green = '\033[92m'
    reset_color = '\033[0m'

    colored_result = color_green + result + reset_color

    print(colored_result)
    print("Area of a rectangle")
    print("Formula: A = length * width")
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print("The area of the rectangle is:", area)

  elif formulam == "3":
    text = "Area of a circle"
    font = "slant"  

    figlet = Figlet(font=font)
    result = figlet.renderText(text)

    color_green = '\033[92m'
    reset_color = '\033[0m'

    colored_result = color_green + result + reset_color

    print(colored_result)
    print("Area of a circle")
    print("Formula: A = π * r²")
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius**2
    print("The area of the circle is:", area)

  elif formulam == "4":
    text = "Perimeter of a rectangle"
    font = "slant"  

    figlet = Figlet(font=font)
    result = figlet.renderText(text)

    color_green = '\033[92m'
    reset_color = '\033[0m'

    colored_result = color_green + result + reset_color

    print(colored_result)
    print("Perimeter of a rectangle")
    print("Formula: P = 2 * (length + width)")
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    perimeter = 2 * (length + width)
    print("The perimeter of the rectangle is:", perimeter)

  elif formulam == "5":
    text = "Circumference of a circle"
    font = "slant"  

    figlet = Figlet(font=font)
    result = figlet.renderText(text)

    color_green = '\033[92m'
    reset_color = '\033[0m'

    colored_result = color_green + result + reset_color

    print(colored_result)
    print("Circumference of a circle")
    print("Formula: C = 2πr")
    radius = float(input("Enter the radius of the circle: "))
    circumference = 2 * math.pi * radius
    print("The circumference of the circle is:", circumference)

  elif formulam == "6":
    text = "Volume of a cube"
    font = "slant"  

    figlet = Figlet(font=font)
    result = figlet.renderText(text)

    color_green = '\033[92m'
    reset_color = '\033[0m'

    colored_result = color_green + result + reset_color

    print(colored_result)
    print("Volume of a cube")
    print("Formula: V = side^3")
    side = float(input("Enter the side of the cube: "))
    volume = side**3
    print("The volume of the cube is:", volume)

  elif formulam == "7":
    text = "Volume of a sphere"
    font = "slant"  

    figlet = Figlet(font=font)
    result = figlet.renderText(text)

    color_green = '\033[92m'
    reset_color = '\033[0m'

    colored_result = color_green + result + reset_color

    print(colored_result)
    print("Volume of a sphere")
    print("Formula: V = (4/3) * π * r^3")
    radius = float(input("Enter the radius of the sphere: "))
    volume = (4/3) * math.pi * radius**3
    print("The volume of the sphere is:", volume)

  elif formulam == "8":
    text = "Distance between two points"
    font = "slant"  

    figlet = Figlet(font=font)
    result = figlet.renderText(text)

    color_green = '\033[92m'
    reset_color = '\033[0m'

    colored_result = color_green + result + reset_color

    print(colored_result)
    print("Distance between two points")
    print("Formula: d = √((x2 - x1)² + (y2 - y1)²)")
    x1 = float(input("Enter the x-coordinate of the first point: "))
    y1 = float(input("Enter the y-coordinate of the first point: "))
    x2 = float(input("Enter the x-coordinate of the second point: "))
    y2 = float(input("Enter the y-coordinate of the second point: "))
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("The distance between the two points is:", distance)

  elif formulam == "9":
    text = "Quadratic Formula"
    font = "slant"  

    figlet = Figlet(font=font)
    result = figlet.renderText(text)

    color_green = '\033[92m'
    reset_color = '\033[0m'

    colored_result = color_green + result + reset_color

    print(colored_result)
    print("Quadratic Formula")
    print("Formula: x = (-b ± √(b^2 - 4ac)) / 2a")
    a = float(input("Enter the coefficient of x^2: "))
    b = float(input("Enter the coefficient of x: "))
    c = float(input("Enter the constant term: "))
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
      x1 = (-b + math.sqrt(discriminant)) / (2*a)
      x2 = (-b - math.sqrt(discriminant)) / (2*a)
      print("The roots of the quadratic equation are:", x1, "and", x2)
    else:
      print("The quadratic equation has no real roots.")

  elif formulam == "10":
    text = "Slope of a line"
    font = "slant"  

    figlet = Figlet(font=font)
    result = figlet.renderText(text)

    color_green = '\033[92m'
    reset_color = '\033[0m'

    colored_result = color_green + result + reset_color

    print(colored_result)
    print("Slope of a line")
    print("Formula: m = (y2 - y1) / (x2 - x1)")
    x1 = float(input("Enter the x-coordinate of the first point: "))
    y1 = float(input("Enter the y-coordinate of the first point: "))
    x2 = float(input("Enter the x-coordinate of the second point: "))
    y2 = float(input("Enter the y-coordinate of the second point: "))
    if x2 - x1 != 0:
      slope = (y2 - y1) / (x2 - x1)
      print("The slope of the line is:", slope)
    else:
      print("The slope of the line is undefined.")

  elif formulam == "11":
    text = "Pythagorean Theorem"
    font = "slant"  

    figlet = Figlet(font=font)
    result = figlet.renderText(text)

    color_green = '\033[92m'
    reset_color = '\033[0m'

    colored_result = color_green + result + reset_color

    print(colored_result)
    print("Pythagorean Theorem")
    print("Formula: c^2 = a^2 + b^2")
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = math.sqrt(a**2 + b**2)
    print("The length of side c is:", c)

  else:
    print("Invalid fromula selected.")

elif subject == "2":
  os.system('cls' if os.name == 'nt' else 'clear')
  formulap = input("Select a formula:\n[1] Force\n[2] Acceleration\n")

else:
  print("Invalid subject selected.")
