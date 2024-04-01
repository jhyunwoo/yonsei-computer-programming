# Temperature Conversion Program (Celsius-Fahrenheit / Fahrenheit-Celsius)

# Display program welcome
print('This program will convert temperatures (Fahrenheit/Celsius)')
print('Enter (F) to convert Fahrenheit to Celsius')
print('Enter (C) to convert Celsius to Fahrenheit')

# Get temperature to convert
which = input('Enter selection: ')

# if temperature to convert is not valid, repeat previous step
while which != 'F' and which != 'C':
    which = input("Please enter 'F' or 'C': ")

# Get temperature from user and convert to int type
temp = int(input('Enter temperature to convert: '))

# if temperature is not valid, repeat previous step
while (which is 'F' and temp < -459.67) or (which is 'C' and temp < -273.15):
    temp = int(input('Enter temperature to convert: '))

# Determine temperature conversion needed and display results
if which == 'F':
    converted_temp = format((temp - 32) * 5/9, '.1f')
    print(temp, 'degrees Fahrenheit equals', converted_temp, 'degrees Celsius')
else:
    converted_temp = format((9/5 * temp) + 32, '.1f')
    print(temp, 'degrees Celsius equals', converted_temp, 'degrees Fahrenheit')


