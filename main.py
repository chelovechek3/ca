s = input("Введите текст:")
a = 0
vowels = set("аеияо")
for letter in s:
    if letter in vowels:
        a += 1
print("Количество гласных:")
print(a)




