# Задача 6.
# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28 и сгенерирует ошибку, если на вход пришла
# невалидная строка.

# Пояснение: если символ встречается 1 раз, он остается без изменений;
# если символ повторяется более 1 раза, к нему добавляется количество повторений.

input_str = str(input("Строка:  "))
res_list = []

def rle(input_str):
    input_str += " "
    temp_letter = input_str[0]
    count_letter = 1
    for ind in range(1, len(input_str)):
        if input_str[ind] == temp_letter:
            count_letter += 1
        else:
            if count_letter == 1:
                res_list.append(f"{temp_letter}")
            else:
                res_list.append(f"{temp_letter}{count_letter}")
            count_letter = 1
            temp_letter = input_str[ind]

if str.isupper(input_str):
    requested_str = rle(input_str)
    print(*res_list, sep="")
else:
    print("Ошибка ввода строки")


# *Задача 3:
# Sample Input
# ["eat", "tea", "tan", "ate", "nat", "bat"]

# Sample output
# [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]

# Т.е. сгруппировать слова по "общим буквам".

def group_letter(input_list):
    word_dict = {}
    for word in input_list:
        if frozenset(word) not in word_dict:
            word_dict[(frozenset(word), len(word))] = [word]
        else:
            word_dict[(frozenset(word), len(word))].append(word)
    res_list = []
    for value in word_dict.values():
        res_list.append(value)
    return res_list

print(["eat", "tea", "tan", "ate", "nat", "bat", "batt", "b", "ba"])
print(group_letter(["eat", "tea", "tan", "ate", "nat", "bat", "batt", "b", "ba"]))






