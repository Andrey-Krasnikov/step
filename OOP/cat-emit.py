import random
import time
class Cat:
    def __init__(self, name, hunger=0, boredom=0, drowsiness=0, thirst=0, health=10):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.drowsiness = drowsiness
        self.thirst = thirst
        self.health = health

    def play(self):
        self.boredom -= 1
        self.hunger += 1
        self.drowsiness += 1
        self.health -= 1

    def eat(self):
        self.hunger -= 1
        self.drowsiness += 1
        self.thirst += 1
        self.health += 1

    def sleep(self):
        self.drowsiness -= 1
        self.health += 1

    def drink(self):
        self.thirst -= 1
        self.boredom +=1

    def __str__(self):
            return f" День из жизни {self.name} подошел к концу. Голод: {self.hunger} Скука: {self.boredom} Усталость: {self.drowsiness} Жажда: {self.thirst} Здоровье: {self.health}"

    def simulate_life(self, days):
        for i in range(days):
            print(f"День {i + 1}:")
            self.hunger += random.randint(-1, 1)
            self.boredom += random.randint(-1, 1)
            self.drowsiness += random.randint(-1, 1)
            self.thirst += random.randint(-1, 1)
            self.health += random.randint(-1, 1)

            if self.health <= 0:
                print(f"{self.name} умер от страшной болезни.")
                return
            if self.hunger <= 0:
                print(f"{self.name} умер от голода. Никто не удосужился купить ему пачку вискаса. Злой народ.")
                return
            if self.thirst >= 5:
                print(f"{self.name} был настолько тупым, что не добрался к водоему.")
                return
            if self.drowsiness >= 5:
                print(f"{self.name} устал. Целыми днями он ловил мышей в подъезде, и ни разу не спал.")
                return
            if self.boredom >= 5:
                print(f" Жизнь вашего кота была слишком скучной. Он умер в скуке и депрессии. Позже его похоронили в коробочке, написав - \n{self.name} 2022-2023.")
                return
            print(self)
            time.sleep(1)
name = input("Введите имя кота:")
my_cat = Cat(name=name, hunger=3, boredom=2, drowsiness=1, thirst=0, health=7)
my_cat.simulate_life(30)
