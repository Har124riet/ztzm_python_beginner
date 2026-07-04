print("Welcome to the Simple Unit Converter!")

# Display options
print("Choose a conversion type:")
print("1. Kilometers to Miles")
print("2. Celsius to Fahrenheit")
print("3. Grams to Pounds")

# User choice
choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    kilometers = float(input("Enter distance in kilometers: "))
    miles = kilometers * 0.621371
    print(f"{kilometers} km is equal to {round(miles, 2)} miles.")

elif choice == "2":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {round(fahrenheit, 1)}°F.")

elif choice == "3":
    grams = float(input("Enter weight in grams: "))
    pounds = grams * 0.00220462
    print(f"{grams} g is equal to {pounds:.2f} lbs.")

else:
    print("Invalid choice. Please run the program again and select 1, 2, or 3.")print("Welcome to the Simple Unit Converter!")

# Display options
print("Choose a conversion type:")
print("1. Kilometers to Miles")
print("2. Celsius to Fahrenheit")
print("3. Grams to Pounds")

# User choice
choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    kilometers = float(input("Enter distance in kilometers: "))
    miles = kilometers * 0.621371
    print(f"{kilometers} km is equal to {round(miles, 2)} miles.")

elif choice == "2":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {round(fahrenheit, 1)}°F.")

elif choice == "3":
    grams = float(input("Enter weight in grams: "))
    pounds = grams * 0.00220462
    print(f"{grams} g is equal to {pounds:.2f} lbs.")

else:
    print("Invalid choice. Please run the program again and select 1, 2, or 3.")