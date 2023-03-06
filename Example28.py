# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def Summa(a,b):
    result = 0
    if b == 0:
        return a
    result = Summa(a,b-1) + 1
    return result

point = True
while point:
    a = int(input("Введите число а больше 0: "))
    b = int(input("Введите число b больше 0: "))
    if a < 0 or b < 0:
        print("a или b меньше 0, введите корректные значения")
        print()
    else:
        point = False

print(f"{a}+{b} = {Summa(a,b)}")