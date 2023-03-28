def get_op():
    op=int(input("Выберите категорию:\n 1 - Импорт данных.\n 2 - Экспорт данных.\n 3 - Изменить данные.\n 4 - Удалить данные.\n 5 - Выход.\n "))
    return op
def get_data():
    print("Введите новые данные")
    name= input("Имя: ")
    surname= input("Фамилия: ")
    telephone= input("Телефон: ")
    data_str= name + " "+ surname +" "+ telephone +"\n"
    return data_str
def find_person():
    data_str = input (" Введите параметр для поиска: ")
    return data_str

def delete_data():
    data_str= input("Введите характеристику для удаления данных: ")
    return data_str

def choose_str():
    answer = int(input("Выберите номер строки: "))
    return answer




