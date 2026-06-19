class Plant:
    def __init__(self, nome, height, age):
        self.name = nome
        self.height = height
        self.age = age

    def age_plant(self, days):
        self.age += days

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f" Color: {self.color}")

        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not blommed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def pruduce_shade(self):
        print(f"Tree {self.name} now produces a shade of {self.height}cm long",
              "and {self.trunk_diameter}cm wide")


class Vegetable(Plant):
    def __init__(self, name, height, age, harverst_season):
        super().__init__(name, height, age)
        self.harverst_seasson = harverst_season
        self.nutritional_value = 0

    def grow(self):
        super().grow()
        self.nutritional_value += 1

    def age_plant(self, days):
        super().age_plant(days)
        self.nutritional_value += days

    def show(self):
        super().show()
        print(f"Harvest season: {self.harverst_seasson}")
        print(f"Nutritional value: {self.nutritional_value}")


print("=== Garden Plant Types ===")
print("=== Flower")

Rose = Flower("Rose", 15, 10, "red")
Rose.show()
print("[asking the rose to bloom]")
Rose.bloom()
Rose.show()
print("\n")

print("=== Tree")
Oak = Tree("Oak", 200, 365, 5)
Oak.show()
print("[asking the oak to produce shade]")
Oak.pruduce_shade()


print("=== Vegetable")
