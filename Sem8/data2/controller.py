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
        if op ==2:
            find_str=view.find_person()
            database.find_person(find_str)
        if op ==3:
            break

