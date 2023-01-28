from random import randint as rand


class Student:
    #print("класс Студнееент")
    col=0 #атрибут класса
    def __init__(self, height=170):
        self.height=height
        #print("Я студент")
        #print(self)
        Student.col+=1 #глобальная
    def grow(self, height=5):
        self.height+=height
student1=Student() #объект класса
print("Количество студентов: ", student1.col)
print("Средний рост студента №1: ",student1.height)
print(student1.col)
student1.grow(height=5)
print(student1.height)
#print(Student.col) #аналогично работает
student2=Student(height=180)
print(student2.col)
print("Количество студентов: ", student2.col)
print("Средний рост студента №2: ",student2.height)
student2.grow(height=15)
print(student2.height)