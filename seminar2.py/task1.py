# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0.56 -> 11

number = input('Введите вещественное число: ')

def sum (number):
    sum = 0
    for i in number:
        if i.isdigit():
            sum = sum + int(i)
    return sum
print (f'Сумма цифр введенного числа = {sum(number)}')