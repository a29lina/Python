# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите число: '))
counter = 0
sum = 0
for n in range(1, n+1):
    sum += (1 + 1/n)**n
    print(round(sum, 3), end=' ')
    counter += 1
print()
print('Сумма равна:', round(sum, 3))