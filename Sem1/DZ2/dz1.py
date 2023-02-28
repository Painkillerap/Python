# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
import os
from random import *
os.system('CLS')
n = int(input('Введите количество монет n: '))
count_orel = 0
count_reshka = 0

for i in range(n):
    x = randrange(0,2,1)
    if x == 0:
        count_orel += 1
    if x == 1:
        count_reshka += 1
if count_reshka > count_orel:
    print(count_orel)
else:
    print(count_reshka)

