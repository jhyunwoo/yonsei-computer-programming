
result = [0, 1]

while len(result) < 100000:
    result.append(result[-1] + result[-2])

print(result)

