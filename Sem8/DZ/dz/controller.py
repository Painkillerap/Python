import os
os.system('CLS')
import view
import database

def main():
    while  True:
        op=view.get_op()
        if op ==1:
            data_worker = view.get_data()
            database.add_data(data_worker)
        elif op ==2:
            find_str=view.find_person()
            database.find_person(find_str)
        elif op==3:
            worker = view.find_person()
            user_lst,full_lst = database.select_data_person(worker)
            num_line = view.choose_str()
            data_worker = view.get_data()
            database.change_data_person(full_lst,user_lst,num_line,data_worker)
            
        elif op==4:
            worker = view.find_person()
            user_lst,full_lst = database.select_data_person(worker)
            num_line = view.choose_str()
            database.delete_data_person(full_lst,user_lst,num_line)
        elif op ==5:
            print("Выход!")
            break

