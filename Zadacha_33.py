# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0

from random import randint

k = int(input("Введите степень k: "))
list = []
for i in range(1, k +2):
    list.append(randint(1, 101)) 

result = []
for i in range(len(list)):
    if k == 1:
        result.append(f'{list[i]}*x')
    elif k == 0:
        result.append(f'{list[i]}')
    else:
        result.append(f'{list[i]}*x^{k}')
    signs = randint(0, 1)
    if signs == 1:
        result.append('+')
    elif signs == 0:
        result.append('-')
    k -= 1

result.pop(-1)
result.append('=0')

rec = open('file_34.txt', 'w')
rec.write(''.join(result))
rec.close()

