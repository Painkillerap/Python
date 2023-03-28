import os
#os.chdir('C:/Uroki/GeekBrains/Python/Seminar/Sem8/data/data.txt')
def write_data(user):
    with open("C:/Uroki/GeekBrains/Python/Seminar/Sem8/data/data.txt", "a") as file:
        file.write(user+"\n")

def find_user(user):
    pass

def read_data():
    with open("C:/Uroki/GeekBrains/Python/Seminar/Sem8/data/data.txt", "r") as f:
        content=f.readlines()
        return(content)

def find_user(lst,str):
    for value in lst:
        if str in value:
            print(value)
