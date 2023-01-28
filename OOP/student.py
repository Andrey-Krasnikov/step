from random import randint as rand


class Student:
    #print("класс Студнееент")
    col=0 #атрибут класса
    def __init__(self, height=170, name=None, age=13):
        self.height=height
        self.name=name
        self.age=age
        #print("Я студент")
        #print(self)
        Student.col+=1 #глобальная
    def grow(self, height=5):
        self.height+=height

    def __str__(self):
        return f"Меня зовут {self.name}. Мне {self.age}"

student1=Student(name="Andrey", age=13) #объект класса
print(student1.__str__())
print(student1.name)
print("Количество студентов: ", student1.col)
print("Рост студента №1: ",student1.height)
student1.grow(height=5)
#print(Student.col) #аналогично работает
student2=Student(height=180, name="NeAndrey")
print("Количество студентов: ", student2.col)
print("Имя студента:",student2.name, ". Средний рост студента №2: ",student2.height, "Возраст студента:", student2.age)
student2.grow(height=15)
print(student2.height)