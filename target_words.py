from operator import itemgetter
def target_words(*letters, words="파이썬은 범용 프로그래밍 언어로 간결하고 쉬운 문법을 가지고 있다"):
    target = []
    words = words + " "
    for letter in letters:
        for i in range(len(words)):
            if words[i] == letter and (words[i+1] == " " or words[i+1] == "," or words[i+1] == "."):
                target_word = ""
                index = i - 1
                while True:
                    if words[index] != " ":
                        target_word += words[index]
                        if index > 0:
                            index -= 1
                        else:
                            break
                    else:
                        break
                target.append(target_word[::-1])
    print_list = []
    while len(target) > 0:
        printing_word = target[0]
        print_list.append([printing_word, target.count(printing_word)])
        while printing_word in target:
            target.remove(printing_word)
    print_list.sort(key=itemgetter(1), reverse=True)
    max_value = print_list[0][1]
    for word in print_list:
        if word[1] == max_value:
            print(f"{word[0]}({word[1]})", end=" ")
    print("")

target_words("은", "로")
target_words("이", words="눈 눈이 와요 눈 눈이 와요 눈이 와요 눈이 와요 창밖에도 눈이 와요")
target_words("는", words="고양이는 밥을 먹고 있고, 강아지는 잠을 자고 있다")
target_words("는", '을', words="어떤 고양이는 밥을 먹고 있고 어떤 고양이는 잠을 자고 있으며 강아지는 잠을 자고 있다")
