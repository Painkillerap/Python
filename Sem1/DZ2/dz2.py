# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
import os 
os.system('CLS')
S = int(input('Введите сумму чисел S: '))
P = int(input('Введите произведение чисел P: '))
for x in range(0,1001):
    for y in range(0,1001):
        if x+y==S and x*y==P:
            print('Числа задуманные Петей:',x,y)