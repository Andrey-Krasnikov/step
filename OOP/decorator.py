def check_call_status(func):
    def wrapper(self, number, *args, **kwargs):
        if self.is_calling:
            print("У вас уже есть один активный звонок.")
        else:
            func(self, number, *args, **kwargs)
    return wrapper


class Phone:
    def __init__(self, number):
        self.number = number
        self.is_calling = False

    @check_call_status
    def call(self, number):
        self.is_calling = True
        print(f"Активный звонок на {number}...")

    def endcall(self):
        self.is_calling = False
        print("Вызов завершен.")


class Smartphone(Phone):
    def __init__(self, number, *args, **kwargs):
        super().__init__(number)
        self.is_connected_to_internet = False
        self.features = kwargs

    def connection(self):
        self.is_connected_to_internet = True
        print("Подключен к интернету.")

    def disconnection(self):
        self.is_connected_to_internet = False
        print("Интернет соединение отключено.")

    def get_feature(self, feature_name):
        return self.features.get(feature_name)

    def set_feature(self, feature_name, value):
        self.features[feature_name] = value
        print(f"{feature_name} установлено значение {value}")



phone = Phone("+380998195599")
smartphone = Smartphone("0956233455", model="Xiaomi Redmi Note 12 Pro Next Gen 6pgn Super speed amolet ", color="rainforest", memory="960GB")

phone.call("0956233455")
phone.call("0996581212")
phone.endcall()

smartphone.set_feature("память", "512KB")
print(smartphone.get_feature("память"))