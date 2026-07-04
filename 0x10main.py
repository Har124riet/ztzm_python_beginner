print("Welcome to the Simple Unit Converter!\n")

# Display options
print("Choose a conversion type:")
print("1. Kilometers to Miles")
print("2. Celsius to Fahrenheit")
print("3. Grams to Pounds")

#  user choice
choice = input("Enter your choice (1/2/3): ")


if choice == "1":
    # Kilometers to Miles
    kilometers = float(input("Enter distance in kilometers: "))
    miles = kilometers * 0.621371  # Conversion factor
    print(f"{kilometers} km is equal to {round(miles, 2)} miles.")

elif choice == "2":
    # Celsius to Fahrenheit
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {round(fahrenheit, 1)}°F")

elif choice == "3":
    # Grams to Pounds
    grams = float(input("Enter weight in grams: "))
    pounds = grams * 0.00220462
    print(f"{grams} g is equal to {round(pounds, 2)} lbs.")

else:
    print("e run the program again and choose 1, 2, or 3.")