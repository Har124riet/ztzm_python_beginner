cities = {"London," "Paris," "Los Angeles," "New York," "Tokyo"}
print(cities)

cities.add("New york")
print(cities)

cities.add("Toronto")
print(cities)

cities.discard("London")
print(cities)

print("/n Cities i have visited:")
for city in cities:
    print(city)

city_to_check = "canada"
if city in cities:
    print(f"\nYes, you have visited {cities}.")
else:
    print(f"\nNo, you have not visited {cities}.")