class Human:
    default_name = "Андрей"
    default_age = 14

    def __init__(self, name=default_name, age=default_age, money=0, house=None):
        self.name = name
        self.age = age
        self.money = money
        self.house = house

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, Money: {self.money}, House: {self.house}")

    @staticmethod
    def default_info():
        print(f"Default name: {Human.default_name}, Default age: {Human.default_age}")

    def __make_deal(self, price):
        if self.money >= price:
            self.money -= price
            return True
        else:
            return False

    def earn_money(self, amount):
        self.money += amount

    def buy_house(self, house, discount=0):
        price = house.final_price(discount)
        if self.__make_deal(price):
            self.house = house
            print("Congratulations, you are a homeowner!")
        else:
            print("Sorry, you do not have enough money to buy this house.")


class House:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def final_price(self, discount):
        return self.price * (1 - discount)


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(area=40, price=price)


# Тестирование
Human.default_info() #Вызовите справочный метод default_info() для класса Human()

person = Human(name="Volodymyr Zelenskiy", age=45, money=20000) #Создайте объект классa Human
person.info() #Выведите справочную информацию о созданном объекте (вызовите метод info()).

house = SmallHouse(price=499000) #Создайте объект класca SmallHouse
person.buy_house(house, discount=0.3) #Попробуйте купить созданный дом, убедитесь в получении предупреждения.

person.earn_money(35000000) #Поправьте финансовое положение объекта вызовите метод earn_money()
person.buy_house(house, discount=0.1) #Снова попробуйте купить дом

person.info() #Посмотрите, как изменилось состояние объекта класca Human
