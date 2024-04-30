n = int(input("Enter a number: "))

look = [1]


def look_and_say(look_list):
    say_list = []
    target = 0
    for num in look_list:
        if len(say_list) <= target:
            say_list.append([1, num])
        else:
            if say_list[target][1] == num:
                say_list[target][0] += 1
            else:
                say_list.append([1, num])
                target += 1
    return sum(say_list, [])


print(look)
for i in range(n):
    look = look_and_say(look)
    print(look)


