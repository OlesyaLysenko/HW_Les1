#Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

number = input("Введиче число: ")
result = int(number) + int((number + number)) + int((number + number + number))
print(result)
