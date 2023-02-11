from random import randint
import time
class Student:
    def __init__(self, name):
        self.name = name
        self.happy = 50
        self.progress = 0
        self.live = True
        self.money = 0

    def study(self):
        print("Время учиться!")
        self.happy -= 10
        self.progress += 5

    def sleep(self):
        print("Время поспать")
        self.happy += 5

    def rest(self):
        print("Время отдыха")
        self.happy += 10
        self.progress -= 5
        self.money -= 5

    def work(self):
        print("Время пахать")
        self.happy -= 5
        self.money += 10

    def islive(self):
        if self.happy <= 0:
            print("Диприссия в 0 лет")
            self.progress = 0
        if self.progress >= 20:
            print("Экзамен сдан.")
            self.happy += 15
            self.progress = 5
        if self.progress < -5:
            print("Экзамен провален! Подготовьтесь еще раз лучше!")
            self.progress = 3
        if self.money < 0:
            print("Кончились деньги, снова пахать на дядю")
            self.work()
            self.progress =-5
            self.happy =-5

    def day(self):
        print("Уровень счастья: ", self.happy)
        print("Успеваемость: ", self.progress)
        print("Деньги: ", self.money)

    def choice(self, numDay):
        numDay = "День #" + str(numDay) + " из жизни " + self.name
        print(f"{numDay:=^50}")
        rnd = randint(1, 4)
        if rnd == 1:
            self.study()
        elif rnd == 2:
            self.sleep()
        elif rnd == 3:
            self.rest()
        else:
            self.work()
        self.day()
        self.islive()

student = Student(name="Андрюши")
for numDay in range(365):
    student.choice(numDay)
    time.sleep(1)

#Теперь, если студент не сдает экзамен/или сдает/впадает в депрессию, имеет шанс из нее выйти, ведь один год - достаточно продолжительный срок, а шанс депрессии, или несдачи - слишком большой.
