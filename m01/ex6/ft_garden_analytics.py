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

        def display(self):
            print(
                f"Stats: {self._grow_call} grow, "
                f"{self._age_call} age, "
                f"{self._show_call} show"
            )


    def age_plant(self, days):
        self.age += days
        self.stats.inc_age()

    @staticmethod
    def check_age(age):
        return age > 365

    @classmethod
    def anonymous(cls):
        return cls("unknown", 0, 0)

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        self.stats.inc_show()


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def grow_flower(self, valor):
        self.height += valor
        self.stats.inc_grow()

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self):
        self.stats.inc_shade()
        
        self.stats.display()
        print(f"{self.stats._shade_call} shade")

        print("[asking the oak to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and {self.trunk_diameter}cm wide."
        )

        print(f"[statistics for {self.name}]")
        self.stats.display()
        print(f"{self.stats._shade_call} shade")


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


print("=== Garden statistics ===")

print("=== Check year-old")
print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
print(f"Is 400 days more than a year? -> {Plant.check_age(400)}")
print("\n")

print("=== Flower")
rose = Flower("Rose", 15.0, 10, "red")
rose.show()
print("[statistics for Rose]")
rose.stats.display()
print("[asking the rose to grow and bloom]")
rose.bloom()
rose.grow_flower(8)
rose.show()
print("[statistics for Rose]")
rose.stats.display()
print("\n")

print("=== Tree")
oak = Tree("Oak", 200.0, 365, 5.0)
oak.show()
print("[statistics for Oak]")
oak.produce_shade()
print("\n")

print("=== Seed")
sunflower = Seed("Sunflower", 80.0, 45, "yellow")
sunflower.show()
print("[make sunflower grow, age and bloom]")
sunflower.height = 110.0
sunflower.age_plant(20)
sunflower.bloom()
sunflower.show()
print("[statistics for Sunflower]")
sunflower.stats.display()
print("\n")


print("=== Anonymous")
unknown = Plant.anonymous()
unknown.show()
print("[statistics for Unknown plant]")
unknown.stats.display()