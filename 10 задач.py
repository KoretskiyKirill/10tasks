#1
try:
    num = int(input('введите число'))
    if num > 0:
        print('число положительное')
except(ValueError):
    print('пиши цифру')
#2
try:
    num = int(input('введите число'))
    if num % 2 == 0:
        print('чётное')
    else:
        print('не чётное')
except(ValueError):
    print('пиши цифру')
#3
try:
    num = int(input('введите число'))
    if 9 < num < 21:
        print('true')
    else:
        print('false')
except(ValueError):
    print('пиши цифру')
#4
try:
    num = int(input('введите число'))
    num_2 = int(input('введите число'))
    if num > 9 and num_2 > 9:
        print('true')
    else:
        print('false')
except(ValueError):
    print('пиши цифру')
#5
try:
    num = int(input('введите число'))
    if num == 0:
        print('0')
    else:
        if num < 0:
            print('отрицательное')
        else:
            print('положительное')
except(ValueError):
    print('пиши цифру')
#6
try:
    num = int(input('введите число'))
    num_2 = int(input('введите число'))
    num_3 = int(input('введите число'))
    if num % 2 == 0 or num_2 % 2 == 0 or num_3 % 2 == 0:
        print("Есть четное число")
except(ValueError):
    print('пиши цифру')
#7
try:
    num = int(input('введите число'))
    if num < 10:
        print('Меньше 10')
    elif num > 9 < 21:
        print('Между 10 и 20')
    elif num > 20:
        print("Больше 20")
except(ValueError):
    print('пиши цифру')
#8
passworld = input('введи пароль')
if passworld == 'passworld1234':
    print("Доступ разрешен")
else:
    print("Доступ запрещен")
#9
try:
    num = int(input('введите число'))
    if num % 400 == 0 or num % 4 == 0 and num % 100 != 0:
        print('високосный')
    else:
        print('не високосный')
except(ValueError):
    print('пиши цифру')
#10
try:
    num = int(input('введите число'))
    num_2 = int(input('введите число'))
    num_3 = int(input('введите число'))
    if num > num_2:
        if num > num_3:
            print(num)
        else:
            print(num_3)
    elif num_2 > num_3:
        print(num_2)
    else:
        print(num_3)
except(ValueError):
    print('пиши цифру')