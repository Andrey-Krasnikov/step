import requests
from bs4 import BeautifulSoup as bs
class Bank():
    def __init__(self, bal = 0, name = "PrivatoFunk"):
        self.bal = bal
        self.name = name

    def dep(self, sum):
        self.bal += sum
        self.history(f"Пополнение на карту {self.name}: {sum}\n")
        print(f"Успешно снято {sum} с вашей карты {self.name}.")

    def withdraw(self, sum):
        if sum > self.bal:
            print(f"Недостаточно средств для снятия с карты {self.name} Текущий баланс: {self.bal} ")
        else:
            self.bal -= sum
            self.history(f"Успешно снято {sum} с вашей карты {self.name}.")
            print(f"Успешно снято {sum} с вашей карты {self.name}.")

    def transfer(self):
        inf = []
        print("Вы можете отправить деньги несколькими способами мгновенных переводов за границу:")
        url = 'https://privatbank.ua/kak-otpravit-dengi-za-granicu'
        res = requests.get(url)
        soup = bs(res.content, 'html.parser')
        res = soup.find_all('div', class_="wrapper clearfix")
        for i in res:
            name_elem = i.find("h2", class_="col-md-7 pull-left wr_inner")
            desc_elem = i.find("p", class_="")
            if name_elem and desc_elem:
                name = name_elem.text.strip()
                description = desc_elem.text.strip()
                inf.append({
                    "Название": name,
                    "Описание": description,
                })
        for i in inf:
            print(f"Название: {i['Название']}\nОписание: {i['Описание']}\n")
    def history(self, operation):
        with open("history.txt", "a") as ops:
            ops.write(operation + "\n")

    def loadhistory(self):
        with open("history.txt", "r") as ops:
            content = ops.read()
            print(f"История с вашей карты:\n {content}")


privat = Bank(2000)

privat.withdraw(200)
privat.transfer()