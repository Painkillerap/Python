# # 1.Создать класс, описывающий человека. Должны быть поля для имени, фамилии и 
# # возраста. Создать экземпляр и вывести информацию о человеке.
# # 2.Доработать предыдущий класс, чтобы вся информация о человеке была доступна 
# # при вызове str над экземпляром.
# # 3.Добавить метод greet, вызов которого будет выводить в консоль информацию о 
# # человеке в формате "Привет! Меня зовут Петров Василий, мне 12 лет".
# # 4.Добавить атрибут grades, в котором будет храниться список оценок. Создать 
# # список учеников, заполняя оценки случайными числами. И вывести информацию о 
# # них в порядке убывания среднего балла. Заполнение оценок и подсчёт среднего 
# # балла вынести в отдельные методы.
# # 5. Создайте класс прямоугольник — Rectangle. Метод __init__ принимает две точки — 
# # левый верхний и правый нижний угол. Каждая точка представлена экземпляром класса 
# # Point. Реализуйте методы вычисления площади и периметра прямоугольника.
# # 6.Добавьте в класс Rectangle метод has_point. Метод принимает точку на 
# # плоскости и возвращает True, если точка находится внутри прямоугольника 
# # и False в противном случае.
# lst = [random.randint(1, 6) for i in range(10)]

# import random
# class Human:
#     def __init__(self,name,surname,age,grades,averages):
#         self.name=name
#         self.surname=surname
#         self.age=age
#         self.grades=grades
#         self.averages=averages
#     def __str__(self):
#         return f"I'm Human {self.name, self.surname, self.age}"
#     def __greet__(self):
#         print(f"Привет! Меня зовут {self.name}{self.surname}, мне {self.age} лет")
#     def grade(self):
#         self.grades=[random.randint(1,5) for i in range(10)]
#     def average(self):
#         return sum(self.grades)/len(self.grades)
#     def __repr__(self):
#         return self.name

# h1_ivan=Human("Ivan","Ivanov", 12,[], 0)
# h2_petr=Human("Petr","Petrov", 13,[], 0)
# h3_semion=Human("Semion","Semiony4", 14,[], 0)
# h4_oleg=Human("Oleg","Olegovi4", 11,[], 0)

# students=[h1_ivan, h2_petr, h3_semion, h4_oleg]
# for i in students:
#     i.grade()
# students.sort(key=lambda x: x.average()) # Сортировка по средней оценке

# print(h1_ivan.name, h1_ivan.surname, h1_ivan.age)
# h1_ivan.__greet__
# h1_ivan.grade()
# #h1_ivan.average()
# print(students)


class Rectangle:
    def area(self):
        return self.d1.x*self.d2.y
    
    def perimetr(self):
        return 2*((self.d2.x-self.d1.x)+(self.d2.y-self.d1.y))
    
class Point:
    def __init__(self,d1,d2):
        self.d1=d1
        self.d2=d2
        
d1=Point(5,2)
d2=Point(4,6)

r=Rectangle(d1,d2)

print(r.area)
print(r.perimetr)