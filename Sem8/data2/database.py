def add_data(data_str):
    with open("C:/Uroki/GeekBrains/Python/Seminar/Sem8/data2/file.txt", "a",encoding="UTF-8") as f:
        f.write(data_str)
        
def find_person(data_str):
    with open("C:/Uroki/GeekBrains/Python/Seminar/Sem8/data2/file.txt", "r",encoding="UTF-8") as f:
        lst_str = f.readlines()
        for worker in lst_str:
            if data_str in worker:
                print(worker)