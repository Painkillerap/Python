# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# line=input().split()
# result={}
# for i in line:
#     if i in result:
#         print(f"{i}_{result[i]}",end=" ")
#     else:
#         print(i,end=" ")
#     result[i]=result.get(i,0)+1
# print(result)

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность не пробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

# text="She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# text_list=text.split()
# result=set()
# for i in text_list:
#     result.add(i.lower())
# print(len(result))
# *доп2
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Сжатие: 111222334 -> 31322414
# aaabbbbbccd -> 3a3b2c1d

# Восстановление: 31322414 ->111222334
# 3a3b2c1d->aaabbbbbccd

#доп*3.)Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.

num=int(input("Введите натуральное число: "))
lst=[]
index=2
while num!=1:
    if num