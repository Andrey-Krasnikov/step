import random
class Tree:
    def __init__(self, info, age, height):
        self.info = info
        self.age = age
        self.height = height

    def grow(self, heightup, ageup):
        self.age += ageup
        self.height += heightup

    def get_info(self):
        print(f"Этому {self.info} - {self.age} лет. Он в длину {self.height} метров")

class FruitTree(Tree):
    def __init__(self, info, age, height, fruit_type):
        super().__init__(info, age, height)
        self.fruit_type = fruit_type
        col = random.randint(0, 170)
        self.col = col

    def sbor(self):
        print(f"Сбор плодов типа {self.fruit_type} с дерева: {self.info}, дал урожай в: {self.col} кг")

    def get_info(self):
        super().get_info()
        print(f"На нем ростут плоды: {self.fruit_type}")

tree = Tree("дубу", 10, 5)
tree.grow(1, 1)
tree.get_info()
print("-------------------------")
fruit_tree = FruitTree("яблоня", 5, 3, "яблоки")
fruit_tree.grow(0.5, 1)
fruit_tree.get_info()
fruit_tree.sbor()