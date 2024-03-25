# Get User Input
base_str = input("What base? ")
power_str = input(f"What power of {base_str}? ")

# Convert string to int
base = int(base_str)
power = int(power_str)

# print result
print(f"{base_str} to the power of {power_str} is {base**power}")
