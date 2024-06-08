from lab13_p8 import MedianSet

s = MedianSet() # create an empty MedianSet
# computeMedian converts int or str to float when computing the median
s.add(10.0)
s.add(30)
s.add("20")
print(s.computeMedian())  # 20.0

# computeMedian returns the median of unique values.
s.add("10")
s.add("+10.000")
print(s == set([10.0, 30, "20", "10", "+10.000"])) # True
print(s.computeMedian())  # 20.0

# MedianSet must not override methods inherited from set class
s.add(10) # set.add ignores this because (10 == 10.0) is True
s.remove("10") # set.remove deletes only the str value "10"
print(s == set([10.0, 20.0, 30.0])) # False
print(s == set([10.0, 30, "20", "+10.000"])) # True
print(s.computeMedian()) # 20.0

# computeMedian returns the mean of the middle with the even number of elements
s.add(40.0)
print(s == set([10.0, 30, "20", "+10.000", 40.0])) # True
print(s.computeMedian()) # 25.0

# computeMedian must raise a ValueError exception for a non-numeric value
s.add("string")
m = s.computeMedian() # ValueError: ...