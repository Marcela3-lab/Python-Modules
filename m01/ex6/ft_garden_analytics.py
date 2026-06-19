class Plant:
    def __init__(self, nome, height, age):
        self.name = nome
        self.height = height
        self.age = age
        self.stats = Plant.Stats()

    class Stats:
        def __init__(self):
            self._grow_call = 0
            self._age_call = 0
            self._show_call = 0
            self._shade_call = 0

        def inc_grow(self):
            self._grow_call += 1

        def inc_age(self):
            self._age_call += 1

        def inc_show(self):
            self._show_call += 1

        def inc_shade(self):
            self._shade_call += 1
            print(f"{self._shade_call}")

        def display(self):
            print(
                f"Stats: {self._grow_call} grow, "
                f"{self._age_call} age, "
                f"{self._show_call} show \n")

    def age_plant(self, days):
        self.age += days

    @staticmethod
    def check_age(age):
        return age > 365

    @classmethod
    def anonymous(cls):
        return cls("unknow")

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self, valor):
        self.height += valor
        self.stats.inc_grow()


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def grow_flower(self, valor):
        super().grow(valor)
        self.stats.inc_grow()

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        self.stats.inc_show()
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not blommed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_count = 0

    def show(self):
        super().show()
        self.stats.inc_show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def pruduce_shade(self):
        self.stats.inc_shade()
        Oak.stats.display()
        print(f"Tree {self.name} now produces a shade of {self.height}cm long",
              "and {self.trunk_diameter}cm wide")


print("=== Garden statiscs ===")
print("Check year-old")
print(f"Is 30 days more than a year --> {Plant.check_age(30)}")
print(f"Is 30 days more than a year --> {Plant.check_age(400)}")
print("\n")
print("=== Flower")
rose = Flower("Rose", 15.0, 10, "red")
rose.show()
print("[Asking the rose to grow and bloom]")
rose.bloom()
rose.grow_flower(8)
rose.show()
print(f"Statics for {rose.name}")
rose.stats.display()
print("\n")
print("=== Tree")
Oak = Tree("Oak", 200, 365, 5.0)
Oak.show()
print(f"Statics for {Oak.name}")
# Oak.grow_tree(2)
Oak.pruduce_shade()

