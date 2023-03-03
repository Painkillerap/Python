# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на
# них выросло различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена
# система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких
# собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения максимального
# числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

import os
os.system('CLS')
n = int(input("Введите количество кустов: "))
a = list(map(int, input(
    "Введите количество ягод на каждом кусте(в строку, по очереди, через пробел): ").split()))
sum_max = 0
for i in range(n):
    sum_1 = sum(a[i:i+3])
    if sum_1 > sum_max:
        sum_max = sum_1
if a[0] + a[-1] + a[-2] > sum_max:
    sum_max = a[0] + a[-1] + a[-2]
if a[0] + a[1] + a[-1] > sum_max:
    sum_max = a[0] + a[1] + a[-1]
print(
    f"Максимальное число ягод, которое можно собрать за один раз равно: {sum_max}")