import string
Capital_letters = string.ascii_uppercase * 2
Smaller_letters = string.ascii_lowercase * 2
st = input()
num = int(input())

result = []

for i in st:
    if i.isupper():
        result.append(Capital_letters[Capital_letters.index(i) - num ])
    elif i == ' ':
        result.append(" ")
    else:
        result.append(Smaller_letters[Smaller_letters.index(i) - num ])

print(''.join(result))