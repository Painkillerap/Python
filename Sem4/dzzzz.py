#16
# n=int(input())
# lst=[]
# for i in range(n):
#     a=int(input())
#     lst.append(a)
# x=int(input())
# print(lst.count(x))


#стоимость слова


word=input().upper()
count=0
if word[0]in "qwertyuiopasdfghjklzxcvbnm":
    for letter in word:
        for letter in points_en.items():
            if letter in value:
                count+=key
else