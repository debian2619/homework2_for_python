# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.

# Пример:

# Для n = 6 -> 14.072

n = int(input())

def create_sequence(n):
    result =  []
    for i in range(1, n + 1 ):
        result.append((1 + 1 / i) ** i)
    return result

def sum_of_list(lst):
    sum_ = 0
    for number in lst:
        sum_+= number
    return sum_
print(round(sum_of_list(create_sequence(n)), 3))


        

