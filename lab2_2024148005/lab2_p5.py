# Temperature conversion program Celsius->Fahrenheit

# program greeting:
print('This program will convert degrees Celsius to degrees Fahrenheit')

# get temperature in Celsius:
celsius = float(input('Enter degrees Celsius: '))

# convert Fahrenheit to Celsius:
fahrenheit = (celsius * 9 / 5)+32

# print result:
print(celsius, 'degrees Celsius equals', format(fahrenheit, '.1f'), 'degrees Fahrenheit')
