# 32. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list = list(map(int, input("Введите числа через пробел:\n").split()))
new_list = []
for i in list:
    if list.count(i)==1:
        new_list.append(i)
print(new_list)

