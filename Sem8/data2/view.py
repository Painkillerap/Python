def get_op():
    op=int(input("Выберите категорию:\n 1 - импорт данных.\n 2 - экспорт данных.\n 3 - изменить данные.\n 4 - удалить данные.\n 5- выход.\n "))
    return op
def get_data():
    name= input("Имя: ")
    surname= input("Фамилия: ")
    telephone= input("Телефон: ")
    data_str= name + " "+ surname +" "+ telephone +"\n"
    return data_str
def find_person():
    data_str = input (" Введите параметр для поиска: ")
    return data_str