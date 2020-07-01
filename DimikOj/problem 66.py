import string
Capital_letters = string.ascii_uppercase * 2
Smaller_letters = string.ascii_lowercase * 2


st = input()

result = []

for i in st:

    # elif i == ' ':
    #     result.append(" ")
    # elif i == ' ':
    #     result.append(" ")

    if i.islower():
        result.append(Smaller_letters[Smaller_letters.index(i) -1 ])
    elif i.isupper():
        result.append(Capital_letters[Capital_letters.index(i)])

print(''.join(result))