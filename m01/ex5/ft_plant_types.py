class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = float(height)
        self.age = age

    def grow(self) -> None:
        self.height += 42

    def age_plant(self, days) -> None:
        self.age += days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")

        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and {self.trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def age_plant(self, days) -> None:
        super().age_plant(days)
        self.nutritional_value += days

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


print("=== Garden Plant Types ===")

print("=== Flower")
rose = Flower("Rose", 15, 10, "red")
rose.show()

print("[asking the rose to bloom]")
rose.bloom()
rose.show()

print()

print("=== Tree")
oak = Tree("Oak", 200, 365, 5)
oak.show()

print("[asking the oak to produce shade]")
oak.produce_shade()

print()

print("=== Vegetable")
tomato = Vegetable("Tomato", 5, 10, "April")
tomato.show()

print("[make tomato grow and age for 20 days]")
tomato.grow()
tomato.age_plant(20)
tomato.show()
