# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
import os
os.system('CLS')
n = int(input('Введите число N: '))
temp = 1
while n > 2*temp:
        temp = temp*2
        print(temp)
