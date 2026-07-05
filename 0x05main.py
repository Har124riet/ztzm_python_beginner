cities = {"London", "Paris", "Los Angeles", "New york", "Tokyo"}
print(cities)

cities.add("New york")
print(cities)

cities.add("Toronto")
print(cities)

cities.discard("London")
print(cities)

print("\n Cities I have visited:")
for city in cities:
    print(city)

city_to_check = "canada"

if city_to_check in cities:
    print(f"\nYes, you have visited {city_to_check}.")
else:
    print(f"\nNo, you have not visited {city_to_check}.")