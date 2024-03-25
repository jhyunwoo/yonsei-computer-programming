a = int(input())
b = int(input())

c = a % b

if c != 0:
    a = b
    b = c
else:
    print(b)

while c != 0:
    c = a % b

    if c != 0:
        a = b
        b = c
    else:
        print(b)