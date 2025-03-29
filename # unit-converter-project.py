# unit-converter-project

from random import choice

def convert_temperature():
    # Converts temperature (Fahrenheit to Celsius)
    fahrenheit = float(input("Enter temperature in F:"))
    celsius = (fahrenheit - 32) * (5/9)
    print(f"Result: {fahrenheit} F is {celsius} C")

def convert_weight():
    # Converts weight (Pounds to Kilograms)
    pound = float(input("Enter weight in pounds: "))
    kilogram = pound * 0.453592
    print(f"Result: {pound} lbs is {kilogram} kg")

def convert_distance():
    # Converts distance (Feet to Meters)
    feet = float(input("Enter distance in feet: "))
    meter = feet * 0.3048
    print(f"Result: {feet} feet is {meter} meters")

def conversion():
    while True:
        print("\nEnter task: 1 = Temperature, 2 = Weight, 3 = Distance (0 to quit):")
        choice = int(input())

        if choice == 1:
            print("OK, let's convert temperature in Fahrenheit to Celsius")
            convert_temperature()
        
        elif choice == 2:
            print("OK, let's convert weight in pound to kg")
            convert_weight()

        elif choice == 3:
            print("OK, let's convert distance in feet to meter")
            convert_distance()

        elif choice == 0:
            print("See you next time!")
            break  # Exit the program

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 0 to quit.")


conversion()
