from random import randint as rand


class Student:
    #print("класс Студнееент")
    def __init__(self, height=170):
        self.height=height
        #print("Я студент")
        #print(self)
student1=Student() #объект класса

print("Средний рост студента №1: ",student1.height)
student2=Student(height=180)
print("Средний рост студента №2: ",student2.height)