import math

# Get number of cities
cities = input("How many cities? ")
cities = int(cities)

# print result
print(f"For {cities} cities, there are {math.factorial(cities)} possible routes")
