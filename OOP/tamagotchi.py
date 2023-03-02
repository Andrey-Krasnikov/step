import time
class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 100
        self.happiness = 100
        self.last_update_time = time.time()

    @property
    def mood(self):
        total = self.hunger + self.happiness
        if total > 200:
            return "счастливым"
        elif total > 100:
            return "нормульно"
        else:
            return "грустно"

    def talk(self):
        about = self.hunger + self.happiness
        if about > 200:
            about =  "я люблю тебя, мой крутой хозяин"
        elif about > 100:
            about = "сижу, лежу. А ты шо?"
        else:
            about = "мне пофик"
        print(f"Разговор с {self.name}: \n     {self.name} сказал вам: {about}\n Статус:")
        self.update_status()

    def feed(self):
        print(f"{self.name} кушает.")
        self.hunger += 10
        self.update_status()

    def play(self):
        print(f"{self.name} играет.")
        self.happiness += 10
        self.update_status()

    def update_status(self):
        current_time = time.time()
        time_since_last_update = current_time - self.last_update_time
        self.hunger -= int(time_since_last_update)
        self.happiness -= int(time_since_last_update)
        self.last_update_time = current_time
        if self.hunger <= 0 or self.happiness <= 0:
            print(f"{self.name} умэр.")
            exit(0)

    def status(self):
        print(f"{self.name} чувствует себя {self.mood}, с пустотой в желудке {self.hunger}, и счастьем на лице {self.happiness}.")

name = input("Назовите своего тамагочэээ\n ")
tamagotchi = Tamagotchi(name)

while True:
    action = input(f"Что сделать с {tamagotchi.name}?\n 1 - Поговорить\n ------------------\n 2 - Накормить \n ------------------\n 3 - Поиграть\n")
    if action == "1":
        tamagotchi.talk()
    elif action == "2":
        tamagotchi.feed()
    elif action == "3":
        tamagotchi.play()
    else:
        print("Неправильный номер. Введите коректное число от 1 до 3.")
    tamagotchi.status()

#Полный прототип настоящего томагочи, разве что, настоящий не настолько крутой. Высчитавается время между прошлым вызовом меню действий, и актуальным. Каждую секунду простоя тамагочи теряет 1 значение своих жизненных параметров. Прописал условия смерти.