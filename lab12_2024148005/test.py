# from lab12_p4 import Fraction
#
# f1 = Fraction(2, 12)
# f2 = Fraction(1, 6)
# f2.num = 2
#
# print('f1:', f1)
# print('f2:', f2)
# f2.reduce()
# print('f2:', f2)
# f2.adjust(3)
# print('f2:', f2)

# from lab12_p5 import Fraction
#
# f1 = Fraction(1, 2) + Fraction(2, 3)
#
# print('f1:', f1)
# f2 = f1 * (-2)
# print('f2:', f2)
# f3 = f2 + 3
# print('f3:', f3)
# try:
#     f4 = f3 + 3.0
#     print('f4:', f4)
# except ValueError:
#     print('f4: value error')

from lab12_p6 import IntCounter

c = IntCounter()
print("count: ", c.count(), "total: ", c.total())
c.insert(1)
print("count: ", c.count(), "total: ", c.total())
c.insert(-2.0)
print("count: ", c.count(), "total: ", c.total())
c.insert(-2.5)
print("count: ", c.count(), "total: ", c.total())
c.insert('3')
print("count: ", c.count(), "total: ", c.total())
c.insert('3.0')
print("count: ", c.count(), "total: ", c.total())
c.insert('x')
print("count: ", c.count(), "total: ", c.total())
c.insert(['4'])
print("count: ", c.count(), "total: ", c.total())
