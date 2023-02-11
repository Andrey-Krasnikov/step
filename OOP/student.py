# from random import randint as rand
#
#
# class Student:
#     #print("класс Студнееент")
#     col=0 #атрибут класса
#     def __init__(self, height=170, name=None, age=13):
#         self.height=height
#         self.name=name
#         self.age=age
#         #print("Я студент")
#         #print(self)
#         Student.col+=1 #глобальная
#     def grow(self, height=5):
#         self.height+=height
#
#     def __str__(self):
#         return f"Меня зовут {self.name}. Мне {self.age}"
#
# student1=Student(name="Andrey", age=13) #объект класса
# print(student1.__str__())
# print(student1.name)
# print("Количество студентов: ", student1.col)
# print("Рост студента №1: ",student1.height)
# student1.grow(height=5)
# #print(Student.col) #аналогично работает
# student2=Student(height=180, name="NeAndrey")
# print("Количество студентов: ", student2.col)
# print("Имя студента:",student2.name, ". Средний рост студента №2: ",student2.height, "Возраст студента:", student2.age)
# student2.grow(height=15)
# print(student2.height)

#СИМУЛЯТОР СТУДЕНТА
from random import randint
class Student:
    def __init__(self, name):
        self.name=name
        self.happy=50
        self.progress=0
        self.live=True

    def study(self):
        print("Время учится")
        self.happy-10
        self.progress+=5
    def sleep(self):
        print("Время сна")
        self.happy+=5
    def rest(self):
        print("Время отдыха")
        self.happy+=10
        self.progress-=5
    def islive(self):
        if self.happy<=0:
            print("Депрессия")
            self.live=False
        if self.progress>=20:
            print("Сессия сдана. Есть больше времени дня отдыха")
            self.happy+=15
            self.live = False
        if self.progress<-5:
            print("Сесстя НЕ СДАНА. Ты отчислен!")
            self.live = False
    def day(self):
        print("Уровень счастья: ", self.happy)
        print("Успеваемость в учебе: ", self.progress)

    def choice(self,numDay):
        numDay="День №"+str(numDay)+"из жизни студента"+self.name
        print(f"{numDay:=^50}")
        rnd=randint(1,3)
        if rnd==1: self.study()
        elif rnd ==2: self.sleep()
        else: self.rest()
        self.day()
        self.islive()

student=Student(name="Андрей")
for numDay in range(7):
    student.choice(numDay)