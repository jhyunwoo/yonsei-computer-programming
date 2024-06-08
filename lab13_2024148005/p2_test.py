from lab13_p2 import AvgList

f = AvgList() # List constructor to create empty list.
f.append(22)
f.append(2.2)
# f.append('2.2')
# Not a numeric type, will raise ValueError exception in computeAvg(): # f.append('2.2')
print(f.computeAvg())
