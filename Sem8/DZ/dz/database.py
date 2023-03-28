def add_data(data_str):
    with open("C:/Uroki/GeekBrains/Python/Seminar/Sem8/DZ/dz/file.txt", "a",encoding="UTF-8") as f:
        f.write(data_str)
        
def find_person(data_str):
    with open("C:/Uroki/GeekBrains/Python/Seminar/Sem8/DZ/dz/file.txt", "r",encoding="UTF-8") as f:
        lst_str = f.readlines()
        for worker in lst_str:
            if data_str in worker:
                print(worker)

def select_data_person(worker):
    user_lst = []
    #a=1
    with open("C:/Uroki/GeekBrains/Python/Seminar/Sem8/DZ/dz/file.txt", "r",encoding="UTF-8") as f:
        full_lst = f.readlines()
        for line in full_lst:
            if worker in line:
                user_lst.append(line)
                #a+=1
    print(*user_lst)
    return user_lst,full_lst

def delete_data_person(full_lst,user_lst,num_line):
    with open("C:/Uroki/GeekBrains/Python/Seminar/Sem8/DZ/dz/file.txt", "w",encoding="UTF-8") as f:
        for line in full_lst:
            if user_lst[num_line-1] != line:
                f.write(line)
            else:
                continue
    print("Удаление завершено!")

def change_data_person(full_lst,user_lst,num_line,data_worker):
        with open("C:/Uroki/GeekBrains/Python/Seminar/Sem8/DZ/dz/file.txt", "w",encoding="UTF-8") as f:
            for line in full_lst:
                if user_lst[num_line-1] != line:
                    f.write(line)
                else:
                    f.write(data_worker)
        print("Изменение завершено!")
