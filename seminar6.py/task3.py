# Задача 3. Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

number = int(input("Введите число: "))
lst = []

for i in range(number):  # Первый вариант
    lst.append((-3)**i)
print(f"Итоговая последовательность: {lst}")


lst = [(-3)**i for i in range(number)] # Второй вариант более короче
print(f"Последовательность применения list comprehension: {lst}")