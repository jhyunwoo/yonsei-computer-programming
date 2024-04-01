#
# Please refer to the slides titled "provided_code_howto.pdf" on how to uncomment and
# execute the below code-snippets in your PyCharm IDE.
#
# You're meant to run this code as we go along in the lecture (your instructor
# will demonstrate this code to you). However, executing it yourself increases
# your learning experience.
#


#
# Ex. 1:
#

# num = float(input('Enter a real number: '))
# if num < 0:
#     num = -num
#     print('num was negative')
# print('The absolute value is', num)



#
# Ex. 2:
#

# first = 1
# second = 2
#
# if first < second:
#     m = first
#     print('First number smaller than  second. ')
# else:
#     m = second
#     print('Second number smaller than first')
#
# print('The smaller number is', m)


#
# Ex. 3:
#

# x = float(input('Enter a number: '))
# y = float(input('Enter a number: '))
# if x == y:
#     print('equal')
#     if y != 0:
#         print('x/y is:', x/y)
# elif x < y:
#     print('x is smaller')
# else:
#     print('y is smaller')
# print('Good bye...')


#
# Ex. 4:
#

# x = float(input('Enter a number: '))
# y = float(input('Enter a number: '))
# if x == y:
#     print('equal')
#
# x == 22
# print('x:', x)


#
# Ex. 5: infinite loop
#        (sum up integers 1..n)
#
# s = 0
# current = 1
# n = int(input('Enter value: '))
# while current <= n:
#     s = s + current
#     # Comment-out following statement for infinite loop:
#     # (Press the PyCharm ``stop'' button to get out of the loop.)
#     current = current + 1
# print('sum 1..' + str(n) + ':', s)


#
# Ex. 6: factorial number computation
#

# fact = 1
#
# n = int(input ('Number >= 0: '))
#
# i = 1    # loop counter
# while i <= n:
#   fact = fact * i
#   i = i + 1
#
# print('The factorial of', n, 'is', fact)


#
# Ex. 7: Boolean flags:
#

ValidInput = False

while not ValidInput:
  choice = int(input('Enter month: '))
  if choice < 1 or choice > 12:
    print('Error: Invalid month!')
  else:
    ValidInput = True
print('Your month: ', choice)
